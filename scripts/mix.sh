#!/usr/bin/env bash
# Mischt einen Musikausschnitt unter ein stummes Reel.
# Aufruf: bash mix.sh <reel-stumm.mp4> <track.wav> <start_sekunden> <out.mp4>
# Fade-in 0,8 s, Fade-out 1,5 s, Lautheit −14 LUFS (zweistufiges loudnorm), AAC 192 kbit/s.
set -euo pipefail
VID="$1"; TRK="$2"; START="$3"; OUT="$4"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$VID")
FO=$(python3 -c "print(max(0.0, float('$DUR')-1.5))")
# Stufe 1: Messung des Ausschnitts
M=$(ffmpeg -v info -ss "$START" -t "$DUR" -i "$TRK" -af "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p')
II=$(echo "$M" | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['input_i'])")
TP=$(echo "$M" | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['input_tp'])")
LRA=$(echo "$M" | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['input_lra'])")
TH=$(echo "$M" | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['input_thresh'])")
# Stufe 2: linearer Abgleich mit den Messwerten, dann Fades
ffmpeg -v error -y -i "$VID" -ss "$START" -t "$DUR" -i "$TRK" \
  -filter_complex "[1:a]loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=$II:measured_TP=$TP:measured_LRA=$LRA:measured_thresh=$TH:linear=true:print_format=summary,afade=t=in:st=0:d=0.8,afade=t=out:st=$FO:d=1.5,aresample=48000[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart "$OUT"
# Kontrolle: integrierte Lautheit des Ergebnisses; bei sehr spitzen Tracks reicht der lineare
# Abgleich nicht (True-Peak-Grenze), dann zweiter Durchlauf mit dynamischem loudnorm (limitiert).
RES=$(ffmpeg -v info -i "$OUT" -af "loudnorm=print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p' | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['input_i'])")
if python3 -c "import sys; sys.exit(0 if float('$RES') < -15.0 else 1)"; then
  ffmpeg -v error -y -i "$VID" -ss "$START" -t "$DUR" -i "$TRK" \
    -filter_complex "[1:a]loudnorm=I=-14:TP=-1.5:LRA=11,afade=t=in:st=0:d=0.8,afade=t=out:st=$FO:d=1.5,aresample=48000[a]" \
    -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart "$OUT"
  RES=$(ffmpeg -v info -i "$OUT" -af "loudnorm=print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p' | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['input_i'])")
  echo "Ergebnis (dynamisch): $RES LUFS"
else
  echo "Ergebnis: $RES LUFS"
fi
