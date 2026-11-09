#!/bin/sh
# Renders every *.mmd here to a cropped PDF, styled by config.json. Usage: cd figs/mermaid && ./render.sh
pup=$(mktemp --suffix=.json)
echo '{"executablePath":"/usr/bin/chromium","args":["--no-sandbox"]}' > "$pup"
for f in *.mmd; do
  mmdc -q -p "$pup" -c config.json -i "$f" -o "${f%.mmd}.pdf" || exit 1
done
rm -f "$pup"
