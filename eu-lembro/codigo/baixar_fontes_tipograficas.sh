#!/usr/bin/env bash
# Baixa as fontes tipográficas usadas nos cartões (Kalam e Archivo, licença SIL OFL 1.1).
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p fonts
base="https://raw.githubusercontent.com/google/fonts/main/ofl"
curl -sSfL "$base/kalam/Kalam-Bold.ttf"    -o fonts/Kalam-Bold.ttf
curl -sSfL "$base/kalam/Kalam-Regular.ttf" -o fonts/Kalam-Regular.ttf
curl -sSfL "$base/archivo/Archivo%5Bwdth,wght%5D.ttf" -o fonts/Archivo.ttf
echo "Fontes salvas em codigo/fonts/"
