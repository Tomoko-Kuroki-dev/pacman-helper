#!/bin/bash
set -e
echo "Instalando pacman-helper..."

mkdir -p "$HOME/.local/share/pacman-helper"
mkdir -p "$HOME/.local/bin"
cp *.py "$HOME/.local/share/pacman-helper/"

cat > "$HOME/.local/bin/pacman-helper" <<'EOF'
#!/bin/bash
cd "$HOME/.local/share/pacman-helper"
exec python3 index.py
EOF

chmod +x "$HOME/.local/bin/pacman-helper"

echo "pacman-helper instalado correctamente."