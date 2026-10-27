#!/usr/bin/env python3
"""Beat-Analyse für Finanzskalpell-Reels.

Aufruf:  python3 -I beat.py <track.wav|m4a> [--dauer 42] [--min-start 15] [--json out.json]
Ausgabe: JSON mit bpm, beat (Sekunden je Schlag), downbeats (Liste), start (empfohlener
         Startpunkt im Track, ein Downbeat in einem stabilen Abschnitt), rms_db des Abschnitts.
Braucht: ffmpeg im PATH, numpy. Keine weiteren Pakete.
"""
import sys, json, subprocess, argparse
import numpy as np

SR = 22050

def decode(path):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32)

def onset_envelope(x, hop=220, win=1024):
    n = (len(x) - win) // hop
    env = np.empty(n, dtype=np.float64)
    bass = np.empty(n, dtype=np.float64)
    w = np.hanning(win)
    freqs = np.fft.rfftfreq(win, 1 / SR)
    bmask = (freqs >= 40) & (freqs <= 150)
    prev = None
    for i in range(n):
        seg = x[i * hop:i * hop + win] * w
        spec = np.abs(np.fft.rfft(seg))
        logspec = np.log1p(spec * 100)
        env[i] = 0.0 if prev is None else np.sum(np.maximum(logspec - prev, 0))
        bass[i] = np.sum(spec[bmask])
        prev = logspec
    env -= env.mean()
    env /= (env.std() + 1e-9)
    return env, bass, hop / SR

def tempo(env, dt, lo=90, hi=140):
    lag_min, lag_max = int(60 / hi / dt), int(60 / lo / dt)
    ac = np.correlate(env, env, mode="full")[len(env) - 1:]
    ac = ac[lag_min:lag_max + 1]
    lag = lag_min + int(np.argmax(ac))
    # Feinabstimmung des Lags über Nachbarn (parabolisch)
    i = lag - lag_min
    if 0 < i < len(ac) - 1:
        a, b, c = ac[i - 1], ac[i], ac[i + 1]
        denom = a - 2 * b + c
        lag = lag + (0.5 * (a - c) / denom if denom else 0)
    beat = lag * dt
    return 60.0 / beat, beat

def phase(env, dt, beat):
    period = beat / dt
    best, best_s = 0.0, -1e9
    for p in np.linspace(0, period, 64, endpoint=False):
        idx = np.arange(p, len(env), period).astype(int)
        s = env[idx].sum()
        if s > best_s:
            best_s, best = s, p
    return best * dt

def downbeat_offset(bass, dt, beat, phi):
    # Welcher der vier Schläge trägt am meisten Bass? Der ist die Eins.
    best, best_s = 0, -1e9
    for k in range(4):
        times = np.arange(phi + k * beat, len(bass) * dt, 4 * beat)
        idx = (times / dt).astype(int)
        idx = idx[idx < len(bass)]
        s = bass[idx].mean() if len(idx) else -1e9
        if s > best_s:
            best_s, best = s, k
    return phi + best * beat

def choose_start(x, downbeats, dauer, min_start):
    total = len(x) / SR
    frame = int(SR * 0.5)
    rms = np.sqrt(np.convolve(x.astype(np.float64) ** 2, np.ones(frame) / frame, mode="same"))
    med = np.median(rms[rms > 1e-4])
    cands = []
    for t in downbeats:
        if t < min_start or t + dauer + 1 > total:
            continue
        seg = rms[int(t * SR):int((t + dauer) * SR)]
        if len(seg) < frame:
            continue
        spread = np.abs(20 * np.log10(seg / med + 1e-9))
        score = -np.percentile(spread, 97) - 0.02 * max(0.0, t - min_start)
        cands.append((score, t, 20 * np.log10(seg.mean() / med + 1e-9)))
    if not cands:
        return None, None
    cands.sort(reverse=True)
    return cands[0][1], cands[0][2]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("track")
    ap.add_argument("--dauer", type=float, default=42.0)
    ap.add_argument("--min-start", type=float, default=15.0)
    ap.add_argument("--json", default=None)
    a = ap.parse_args()
    x = decode(a.track)
    env, bass, dt = onset_envelope(x)
    bpm, beat = tempo(env, dt)
    phi = phase(env, dt, beat)
    d0 = downbeat_offset(bass, dt, beat, phi)
    downbeats = list(np.arange(d0, len(x) / SR, 4 * beat))
    start, rel_db = choose_start(x, downbeats, a.dauer, a.min_start)
    out = {
        "track": a.track, "dauer_track": round(len(x) / SR, 2),
        "bpm": round(bpm, 2), "beat": round(beat, 4), "bar": round(4 * beat, 4),
        "first_downbeat": round(float(d0), 3),
        "start": None if start is None else round(float(start), 3),
        "abschnitt_rel_db": None if rel_db is None else round(float(rel_db), 2),
        "downbeats": [round(float(t), 3) for t in downbeats[:64]],
    }
    s = json.dumps(out, ensure_ascii=False, indent=1)
    if a.json:
        open(a.json, "w").write(s)
    print(s)

if __name__ == "__main__":
    main()
