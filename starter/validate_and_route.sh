#!/usr/bin/env bash
#
# validate_and_route.sh
#
# Purpose:
# - Validate JSON files in the raw/ directory
# - Track valid files
# - Copy invalid files to invalid/
#
# NOTE:
# This file contains starter code only.
# You are expected to complete the TODO sections.

set -uo pipefail

RAW_DIR="raw"
INVALID_DIR="invalid"
VALID_FILE_LIST="valid_files.txt"

# Create required directories
mkdir -p "$INVALID_DIR" "logs"

# Clean up invalid/ so the script is safely re-runnable
rm -f "$INVALID_DIR"/*.json 2>/dev/null

LOGS_DIR="logs"
TODAY="$(date -u +"%Y-%m-%d")"
log_file="$LOGS_DIR/$TODAY.log"

> "$VALID_FILE_LIST"

shopt -s nullglob

for file in "$RAW_DIR"/*.json; do
    [[ -f "$file" ]] || continue

    echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] validate_and_route.sh: validating '$file'" >> "$log_file"

    python3 validate_json.py "$file"
    status=$?

    if [[ "$status" -eq 0 ]]; then
        echo "$file" >> "$VALID_FILE_LIST"
        echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] validate_and_route.sh: valid '$file'" >> "$log_file"
    else
        cp "$file" "$INVALID_DIR/"
        echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] validate_and_route.sh: invalid, copied to '$INVALID_DIR/$(basename "$file")'" >> "$log_file"
    fi
done
