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

echo "Pipeline started."

echo "Starting filename organization (organize_files.sh)..."
./organize_files.sh

echo "Starting validation and routing (validate_and_route.sh)..."
./validate_and_route.sh

echo "Starting JSON processing (process_jsons.py)..."
python3 process_jsons.py

echo "Starting dataset merge (merge_to_dataset.py)..."
python3 merge_to_dataset.py

echo "Pipeline completed successfully."
