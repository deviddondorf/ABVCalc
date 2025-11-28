#!/bin/sh
# main-launcher.sh - stabil für Flatpak + PySide6

# Python-Modulpfad
export PYTHONPATH=/app/lib/python3.11/site-packages

# Qt-Plugins
export QT_PLUGIN_PATH=/app/lib/python3.11/site-packages/PySide6/Qt/plugins

# Qt Plattform-Fallback
export QT_QPA_PLATFORM=wayland;xcb

# Python-Home setzen (optional, kann Probleme verhindern)
export PYTHONHOME=/app

# Starten der App
exec python3 /app/share/abv-calculator/main.py

