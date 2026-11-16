#!/usr/bin/env bash
# sprechreel-mix.sh <reel.mp4> <voice.m4a|wav> <ausgabe.mp4> [voice_offset_s] [lead_s]
# Fassung 1 (16.11.2026): Stimme aufbereiten (Hochpass 80 Hz, afftdn, Kompressor), Soundeffekte des
# ChatGPT-Reels per Sidechain unter der Stimme um rund 10 dB absenken, in Sprechpausen voll;
# zweistufiges loudnorm -14 LUFS, Spitzen -1 dBTP; Stimme länger als Video: letztes Bild einfrieren.
# voice_offset_s: Stille am Anfang der Aufnahme wegschneiden (Standard: automatisch, erster Ton minus lead_s)
set -euo pipefail
V="$1"; A="$2"; OUT="$3"; OFF="${4:-auto}"; LEAD="${5:-0.4}"
T=$(mktemp -d)
if [ "$OFF" = "auto" ]; then
  S=$(ffmpeg -v info -i "$A" -af "silencedetect=n=-35dB:d=0.3" -f null /dev/null 2>&1 | grep -m1 -oE "silence_end: [0-9.]+" | awk '{print $2}')
  if [ -z "${S:-}" ]; then OFF=0; else OFF=$(python3 -c "print(max(0.0, $S - $LEAD))"); fi
fi
# Stimme: schneiden, aufbereiten, Endstille auf 0,8 s kürzen
ffmpeg -y -v error -ss "$OFF" -i "$A" -af "highpass=f=80,afftdn=nr=12:nf=-30,acompressor=threshold=-20dB:ratio=3:attack=8:release=160:makeup=4,silenceremove=stop_periods=-1:stop_duration=0.8:stop_threshold=-38dB:detection=peak:stop_silence=0.8,aresample=48000,aformat=channel_layouts=stereo" "$T/voice.wav"
DV=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$T/voice.wav")
DX=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
echo "Stimme ${DV}s (ab ${OFF}s der Aufnahme), Video ${DX}s"
PAD=$(python3 -c "print(max(0.0, $DV + 0.3 - $DX))")
# Video ggf. verlängern (letztes Bild einfrieren), Tonspur des Reels herausziehen
ffmpeg -y -v error -i "$V" -vf "tpad=stop_mode=clone:stop_duration=$PAD" -an -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -r 30 "$T/video.mp4"
ffmpeg -y -v error -i "$V" -af "apad=pad_dur=$PAD,aresample=48000,aformat=channel_layouts=stereo" "$T/sfx.wav"
# Mix: SFX per Sidechain unter der Stimme absenken, dann summieren
FILTER="[1:a]asplit=2[vc][vm];[0:a][vc]sidechaincompress=threshold=0.02:ratio=8:attack=25:release=450:makeup=1[sfx];[sfx][vm]amix=inputs=2:duration=longest:normalize=0:weights=1 1.6[mix]"
ffmpeg -y -v error -i "$T/sfx.wav" -i "$T/voice.wav" -filter_complex "$FILTER" -map "[mix]" "$T/mix.wav"
# loudnorm zweistufig
J=$(ffmpeg -v info -i "$T/mix.wav" -af "loudnorm=I=-14:TP=-1:LRA=11:print_format=json" -f null /dev/null 2>&1 | sed -n '/^{/,/^}/p')
II=$(echo "$J" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['input_i'],d['input_tp'],d['input_lra'],d['input_thresh'],d['target_offset'])")
set -- $II
ffmpeg -y -v error -i "$T/video.mp4" -i "$T/mix.wav" -filter_complex "[1:a]loudnorm=I=-14:TP=-1:LRA=11:measured_I=$1:measured_TP=$2:measured_LRA=$3:measured_thresh=$4:offset=$5:linear=true:print_format=summary,aresample=48000[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart "$OUT"
ffmpeg -v info -i "$OUT" -af "loudnorm=I=-14:TP=-1:LRA=11:print_format=json" -f null /dev/null 2>&1 | sed -n '/^{/,/^}/p' | python3 -c "import json,sys; d=json.load(sys.stdin); print('Ergebnis', d['input_i'],'LUFS, TP', d['input_tp'])"
ffprobe -v error -show_entries format=duration:stream=codec_name,width,height -of compact "$OUT"
rm -rf "$T"
