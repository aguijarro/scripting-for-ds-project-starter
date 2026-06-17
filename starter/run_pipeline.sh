#!/usr/bin/env bash
#
# run_pipeline.sh
#
# Purpose:
# Run the full data processing pipeline from start to finish.
#
# NOTE:
# This file contains starter code only.
# You are expected to complete the TODO sections.

set -euo pipefail

cd "$(dirname "$0")"

LOGS_DIR="logs"
TODAY="$(date -u +"%Y-%m-%d")"
log_file="$LOGS_DIR/$TODAY.log"
mkdir -p "$LOGS_DIR"

log() {
    echo "$(date -u +"%Y-%m-%dT%H:%M:%SZ") - run_pipeline.sh: $1" >> "$log_file"
}

trap 'log "pipeline failed"' ERR

log "pipeline started"

log "running organize_files.sh"
./organize_files.sh

log "running validate_and_route.sh"
./validate_and_route.sh

log "running process_jsons.py"
python3 process_jsons.py

log "running merge_to_dataset.py"
python3 merge_to_dataset.py

log "pipeline completed successfully"
