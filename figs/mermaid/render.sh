#!/bin/sh
# Renders every *.mmd here to a cropped PDF, styled by config.json. Usage: cd figs/mermaid && ./render.sh
# A private fontconfig adds TeX Live's Latin Modern Sans (= beamer's CM Sans) without installing it system-wide.
tmp=$(mktemp -d)
echo '{"executablePath":"/usr/bin/chromium","args":["--no-sandbox"]}' > "$tmp/pup.json"
cat > "$tmp/fonts.conf" <<EOF
<?xml version="1.0"?>
<fontconfig>
  <include ignore_missing="yes">/etc/fonts/fonts.conf</include>
  <dir>$(dirname "$(kpsewhich lmsans10-regular.otf)")</dir>
  <cachedir>$tmp/cache</cachedir>
</fontconfig>
EOF
for f in *.mmd; do
  FONTCONFIG_FILE="$tmp/fonts.conf" mmdc -q -p "$tmp/pup.json" -c config.json -i "$f" -o "${f%.mmd}.pdf" || exit 1
done
rm -rf "$tmp"
