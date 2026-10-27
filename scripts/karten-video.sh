#!/usr/bin/env bash
# Karten-Video: beliebige Bilder (1080×1350-Karten, Grafiken) als 9:16-Video mit Wisch-Übergang (stumm).
# Aufruf: bash karten-video.sh <out-stumm.mp4> <bild1> <dauer1> <bild2> <dauer2> [...]
# Beispiele (Vorgabe 26.10.2026):
#   Schätz-Video:  bash karten-video.sh schaetz-stumm.mp4 schaetz-01.jpg 7.0 schaetz-02.jpg 5.0
#   Grafik-Video:  bash karten-video.sh grafik-stumm.mp4 karte-01.jpg 3.6 grafik.jpg 7.0
# Jedes Bild wird in 1080×1920 eingepasst (Seitenverhältnis bleibt), Rest #14171D (dunkles Papier);
# Übergang slideleft 0,6 s, 30 fps, h264 crf 18. Gesamtlänge = Summe der Dauern − 0,6 s je Übergang.
set -euo pipefail
OUT="$1"; shift
X=0.6; FPS=30
if [ $(( $# % 2 )) -ne 0 ] || [ $# -lt 2 ]; then echo "Aufruf: karten-video.sh <out> <bild> <dauer> [<bild> <dauer> ...]" >&2; exit 1; fi
inputs=(); filt=""; durs=(); i=0
while [ $# -gt 0 ]; do
  f="$1"; d="$2"; shift 2
  inputs+=(-loop 1 -t "$d" -framerate $FPS -i "$f"); durs+=("$d")
  filt+="[$i:v]scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x14171D,format=yuv420p,setsar=1[v$i];"
  i=$((i+1))
done
N=$i
prev="v0"; total=${durs[0]}
for ((k=1;k<N;k++)); do
  off=$(python3 -c "print(round($total-$X,3))")
  filt+="[$prev][v$k]xfade=transition=slideleft:duration=$X:offset=$off[x$k];"
  prev="x$k"; total=$(python3 -c "print(round($total-$X+${durs[$k]},3))")
done
filt="${filt%;}"
ffmpeg -v error -y "${inputs[@]}" -filter_complex "$filt" -map "[$prev]" -r $FPS -c:v libx264 -crf 18 -pix_fmt yuv420p -movflags +faststart "$OUT"
echo "Länge $total s, $N Bilder"
