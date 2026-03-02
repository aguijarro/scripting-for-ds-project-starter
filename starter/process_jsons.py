#!/usr/bin/env python3

import json
import os
import shutil
import datetime

# ---------- logging ----------
LOGS_DIR = "logs"
TODAY = datetime.datetime.utcnow().strftime("%Y-%m-%d")
LOG_FILE = os.path.join(LOGS_DIR, f"{TODAY}.log")
os.makedirs(LOGS_DIR, exist_ok=True)

def log(message):
    """
    TODO:
    Implement this function to write a timestamped log message
    to the daily log file.

    Format:
    YYYY-MM-DDTHH:MM:SSZ - process_jsons.py: <message>
    """
    # TODO:
    # 1. Generate a UTC timestamp
    # 2. Open LOG_FILE in append mode
    # 3. Write the formatted log message
    pass
# -----------------------------

RAW_DIR = "raw"
CLEAN_DIR = "clean"
ARCHIVE_DIR = "archive"
VALID_FILES = "valid_files.txt"

os.makedirs(CLEAN_DIR, exist_ok=True)
os.makedirs(ARCHIVE_DIR, exist_ok=True)

# Clean up clean/ and archive/ so the script is safely re-runnable
for _f in os.listdir(CLEAN_DIR):
    if _f.endswith(".json"):
        os.remove(os.path.join(CLEAN_DIR, _f))
for _f in os.listdir(ARCHIVE_DIR):
    if _f.endswith(".json"):
        os.remove(os.path.join(ARCHIVE_DIR, _f))

# ---------- load valid file list ----------

# TODO:
# Check if VALID_FILES exists.
# If it does not exist:
# - Write a log entry
# - Exit the script with a non-zero status
#


# TODO:
# Open VALID_FILES and read all non-empty lines into a list called `files`.
#


# TODO:
# Write a log entry indicating how many files will be processed.
#
# log("...")

# ---------- normalize one JSON ----------
def normalize_json(data):
    """
    Normalize a single JSON record into a consistent structure.
    """

    cleaned = {}

    # TODO:
    # Extract product_id.
    # Use the top-level key if present,
    # otherwise look inside data["product"]["id"].
    #

    # TODO:
    # Extract name.
    # Use the top-level key if present,
    # otherwise look inside data["product"]["name"].
    #

    # TODO:
    # Extract category.
    # Use "unknown" if not present.
    #

    # TODO:
    # Extract price and convert to float.
    # If conversion fails, use 0.0.
    #

    # TODO:
    # Extract metadata fields:
    # - color
    # - stock (default to 0)
    #


    # TODO:
    # Extract created_at.
    # Use metadata["created_at"] if present,
    # otherwise use metadata["created"].
    #

    return cleaned

# ---------- process each file ----------

# TODO:
# Loop over each file path in `files`.
#
# for file_path in files:

    # TODO:
    # Extract the filename from the file path.
    #
    # filename = ...

    # TODO:
    # Open and load the JSON file.
    # If reading fails:
    # - Write a log entry
    # - Skip to the next file

    # TODO:
    # Normalize the JSON data.
    #
    # cleaned_data = ...

    # TODO:
    # Write the cleaned JSON to the clean/ directory with indent=2.


    # TODO:
    # Write a log entry indicating the cleaned file was written.
    #
    # log("...")

    # TODO:
    # Copy the original file to the archive/ directory.
    #
    # archive_path = ...


    # TODO:
    # Write a log entry indicating the file was archived.
    #
    # log("...")

# TODO:
# Write a log entry indicating that processing is complete.
#
# log("Processing complete")