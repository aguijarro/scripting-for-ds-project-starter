#!/usr/bin/env bash
# organize_files.sh
#
# Purpose:
# - Normalize filenames
# - Add a timestamp
# - Copy files into the raw/ folder
#
# NOTE:
# This file contains starter code only.
# You are expected to complete the TODO sections.

set -uo pipefail

RAW_DIR="raw"
DUMPS_DIR="json_dump"

# --- Daily logging setup ---
LOGS_DIR="logs"
TODAY="$(date -u +"%Y-%m-%d")"
log_file="$LOGS_DIR/$TODAY.log"
mkdir -p "$LOGS_DIR"

echo "$(date -u +"%Y-%m-%dT%H:%M:%SZ") - organize_files.sh: started" >> "$log_file"

# Create raw directory if it doesn't exist
mkdir -p "$RAW_DIR"

# Clean up raw/ so the script is safely re-runnable (clear entire output dir)
rm -f "$RAW_DIR"/* 2>/dev/null

# Ensure the loop does not fail if the folder is empty
shopt -s nullglob

for src in "$DUMPS_DIR"/*; do
    [ -f "$src" ] || continue

    base="$(basename "$src")"
    base_lower="${base,,}"

    # Product dump files use a product-style name (any extension); skip support files.
    case "$base_lower" in
        readme.md) continue ;;
        product*) ;;
        *) continue ;;
    esac

    newname="$(echo "$base_lower" | sed 's/[ -]/_/g')"

    name_without_ext="${newname%.*}"

    ts="$(date -u +"%Y%m%dT%H%M%SZ")"

    final_name="${name_without_ext}_${ts}.json"

    cp "$src" "$RAW_DIR/$final_name"

    echo "$(date -u +"%Y-%m-%dT%H:%M:%SZ") - organize_files.sh: copied $src -> $RAW_DIR/$final_name" >> "$log_file"

done

echo "$(date -u +"%Y-%m-%dT%H:%M:%SZ") - organize_files.sh: finished" >> "$log_file"
