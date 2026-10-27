#!/usr/bin/env bash
# Animiertes Karussell: Karten 1080×1350 als 9:16-Video mit Wisch-Übergang (stumm).
# Aufruf: bash karussell-video.sh <out-stumm.mp4> <karte-01.jpg> … <karte-08.jpg>
# Zeiten: Cover 3,6 s, jede weitere Karte 5,0 s, Übergang slideleft 0,6 s; Hintergrund #14171D (dunkles Papier).
set -euo pipefail
OUT="$1"; shift
N=$#; COVER=3.6; CARD=5.0; X=0.6; FPS=30
inputs=(); filt=""; i=0
for f in "$@"; do
  d=$CARD; [ $i -eq 0 ] && d=$COVER
  inputs+=(-loop 1 -t "$d" -framerate $FPS -i "$f")
  filt+="[$i:v]scale=1080:1350,pad=1080:1920:0:285:color=0x14171D,format=yuv420p,setsar=1[v$i];"
  i=$((i+1))
done
# xfade-Kette: Offset = bisherige Gesamtlänge − Übergang
prev="v0"; total=$COVER
for ((k=1;k<N;k++)); do
  off=$(python3 -c "print(round($total-$X,3))")
  filt+="[$prev][v$k]xfade=transition=slideleft:duration=$X:offset=$off[x$k];"
  prev="x$k"; total=$(python3 -c "print(round($total-$X+$CARD,3))")
done
filt="${filt%;}"
ffmpeg -v error -y "${inputs[@]}" -filter_complex "$filt" -map "[$prev]" -r $FPS -c:v libx264 -crf 18 -pix_fmt yuv420p -movflags +faststart "$OUT"
echo "Länge $total s, $N Karten"
