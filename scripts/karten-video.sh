#!/usr/bin/env bash
# karten-video.sh — baut aus beliebig vielen Karten (1080×1350) ein stummes 9:16-Video (1080×1920):
# jede Karte mittig auf dunklem Papier #14171D, Wisch-Übergang slideleft 0,6 s.
# Verallgemeinerung von karussell-video.sh (Cover 3,6 s, Karten 5,0 s) für Schätz-Video und Grafik-Video.
#
# Aufruf:
#   bash karten-video.sh <ausgabe.mp4> <dauer1> <karte1.jpg> [<dauer2> <karte2.jpg> ...]
# Beispiele:
#   Schätz-Video:   bash karten-video.sh schaetz-stumm.mp4 7.0 schaetz-01.jpg 5.0 schaetz-02.jpg
#   Grafik-Video:   bash karten-video.sh grafik-stumm.mp4 3.6 karte-01.jpg 7.0 grafik-01.jpg
#   Karussell:      bash karten-video.sh karussell-stumm.mp4 3.6 karte-01.jpg 5.0 karte-02.jpg ... 5.0 karte-08.jpg
# Gesamtlänge = Summe der Dauern (die Übergänge liegen innerhalb der Dauern, wie bei karussell-video.sh: 34,4 s bei 3,6 + 7 × 5,0 − 7 × 0,6).
# Danach wie gewohnt: beat.py --dauer <Länge>, mix.sh <stumm> <track.wav> <start> <ausgabe>.

set -euo pipefail
out="$1"; shift
XF=0.6
inputs=(); durs=()
while [ $# -gt 0 ]; do
  durs+=("$1"); inputs+=("$2"); shift 2
done
n=${#inputs[@]}
[ "$n" -ge 1 ] || { echo "mindestens eine Karte" >&2; exit 1; }

args=()
for i in $(seq 0 $((n-1))); do
  args+=(-loop 1 -t "${durs[$i]}" -i "${inputs[$i]}")
done

filter=""
for i in $(seq 0 $((n-1))); do
  filter+="[$i:v]scale=1080:-2:flags=lanczos,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=#14171D,setsar=1,format=yuv420p,fps=30[v$i];"
done

if [ "$n" -eq 1 ]; then
  filter+="[v0]copy[vout]"
else
  prev="v0"; offset=0
  for i in $(seq 1 $((n-1))); do
    offset=$(python3 -c "print(round($offset + ${durs[$((i-1))]} - $XF, 3))")
    label="x$i"; [ "$i" -eq $((n-1)) ] && label="vout"
    filter+="[$prev][v$i]xfade=transition=slideleft:duration=$XF:offset=$offset[$label];"
    prev="$label"
  done
  filter="${filter%;}"
fi

ffmpeg -y "${args[@]}" -filter_complex "$filter" -map "[vout]" -an \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -movflags +faststart "$out"
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,duration -of default=nw=1 "$out"
