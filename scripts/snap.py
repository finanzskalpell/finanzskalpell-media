#!/usr/bin/env python3
"""Rundet die Szenenwechsel eines Reels auf das Beat-Raster der Musik.

Aufruf: python3 -I snap.py reel.html <beat_sekunden> [--toleranz 0.25]
Die Musik startet bei Reel-Sekunde 0 auf einem Downbeat (so mischt mix.sh), das Raster ist
also k * beat. Jeder Szenenbeginn ab Szene 2 wird auf den nächsten Beat gezogen, wenn der
Abstand höchstens --toleranz beträgt; das Ende der Vorszene folgt mit 0,4 s Überlappung.
Das Ende der letzten Szene (Gesamtlänge) bleibt. Schreibt reel.html in place, druckt alt/neu.
"""
import re, sys, argparse

ap = argparse.ArgumentParser()
ap.add_argument("html"); ap.add_argument("beat", type=float)
ap.add_argument("--toleranz", type=float, default=0.25)
a = ap.parse_args()
src = open(a.html, encoding="utf-8").read()
m = re.search(r"const SC=\[(.*?)\];", src)
if not m:
    sys.exit("SC-Array nicht gefunden")
pairs = re.findall(r"\{in:([\d.]+),out:([\d.]+)\}", m.group(1))
sc = [[float(i), float(o)] for i, o in pairs]
X = 0.4
changed = []
for k in range(1, len(sc)):
    start = sc[k][0] + X  # sichtbarer Wechsel = Ende der Vorszene (in + Überlappung)
    beat_k = round(start / a.beat)
    target = beat_k * a.beat
    if abs(target - start) <= a.toleranz and target - X > sc[k - 1][0] + 1.0:
        sc[k][0] = round(target - X, 2)
        sc[k - 1][1] = round(target, 2)
        changed.append((k, round(start, 2), round(target, 2)))
new = "const SC=[" + ",".join("{in:%s,out:%s}" % (i, o) for i, o in sc) + "];"
src = src[:m.start()] + new + src[m.end():]
open(a.html, "w", encoding="utf-8").write(src)
print("Beat %.4f s · Wechsel verschoben:" % a.beat, changed if changed else "keine")
print(new)
