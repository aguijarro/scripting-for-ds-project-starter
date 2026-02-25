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

# TODO:
# Write a log entry indicating that organize_files.sh has started.
# Include a UTC timestamp.
#
# echo "..." >> "$log_file"
# ----------------------------

# Create raw directory if it doesn't exist
mkdir -p "$RAW_DIR"

# Clean up raw/ so the script is safely re-runnable
rm -f "$RAW_DIR"/*.json 2>/dev/null

# Ensure the loop does not fail if the folder is empty
shopt -s nullglob

for src in "$DUMPS_DIR"/*; do

    base="$(basename "$src")"

    # TODO 1:
    # Convert the filename to lowercase
    # Hint: look up the `tr` command
    #
    # newname="..."

    # TODO 2:
    # Replace spaces and hyphens with underscores
    # Hint: look up the `sed` command
    #
    # newname="..."

    # TODO 3:
    # Remove the file extension
    # (assume files may have inconsistent extensions)
    #
    # name_without_ext="..."

    # TODO 4:
    # Generate a UTC timestamp in the format:
    # YYYYMMDDTHHMMSSZ
    #
    # ts="..."

    # TODO 5:
    # Construct the final filename using:
    # <clean_name>_<timestamp>.json
    #
    # final_name="..."

    # TODO 6:
    # Copy the file into the raw/ directory with the new name
    #
    # TODO 7:
    # Write a log entry for the file copy.
    # Include:
    # - UTC timestamp
    # - source file path
    # - destination file path
    
done

# TODO:
# Write a log entry indicating that organize_files.sh has finished.
# Include a UTC timestamp.
