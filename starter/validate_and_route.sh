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

# TODO:
# Clear the contents of VALID_FILE_LIST so it starts empty.
#
# > "$VALID_FILE_LIST"

for file in "$RAW_DIR"/*.json; do
    # TODO:
    # Skip the loop iteration if the file does not exist.

    # TODO:
    # Write a log entry indicating validation is starting for this file.
    # Include a UTC timestamp and the file path.
    
    # TODO:
    # Run the validate_json.py script on the file.
    
    # TODO:
    # Capture the exit status of the validation script.
    
    # TODO:
    # If the status is 0:
    # - Append the file path to VALID_FILE_LIST
    # - Write a log entry indicating the file is valid
    #
    # Otherwise:
    # - Copy the file to INVALID_DIR
    # - Write a log entry indicating the file was copied to invalid
    #
done