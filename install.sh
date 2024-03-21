#!/bin/bash

REPO="https://codeberg.org/WinFan3672/fb.git"
TEMPDIR="/tmp/fb"
DATADIR="/usr/share/fb"
BINFILE="/bin/fb"

main() {
    echo "Cloning repo..."
    ## Clone the repo
    git clone "$REPO" "$TEMPDIR"
    cd "$TEMPDIR" || exit 1
    ## Copy files
    echo "Copying files..."
    mkdir "$DATADIR" || sleep 0
    cp app.css "$DATADIR/app.css"
    cp main.py "$BINFILE"
    chmod +x "$BINFILE"
    echo "Installation complete! Run fb to see if it works!"
}

# Checks if root
# If not, runs sudo
if [ "$EUID" -ne 0 ]; then
    sudo sh "$0" "$@"
    exit $?
fi

main

