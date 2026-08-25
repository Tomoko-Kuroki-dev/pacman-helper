#!/bin/bash
set -e
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
echo "Instalando pacman-helper..."

if ! command -v python3 >/dev/null; then
    echo "Error: Python 3 no está instalado."
    exit 1
fi
if ! command -v pacman >/dev/null; then
    echo "Error: pacman no está disponible."
    exit 1
fi

mkdir -p "$HOME/.local/share/pacman-helper"
mkdir -p "$HOME/.local/bin"
cp "$SCRIPT_DIR"/*.py "$HOME/.local/share/pacman-helper/"
cat > "$HOME/.local/bin/pacman-helper" <<'EOF'
#!/bin/bash

cd "$HOME/.local/share/pacman-helper"
exec python3 index.py
EOF

chmod +x "$HOME/.local/bin/pacman-helper"
echo "pacman-helper instalado correctamente."