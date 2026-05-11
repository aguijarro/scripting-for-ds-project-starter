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
    Write a timestamped log message to the daily log file.

    Format:
    YYYY-MM-DDTHH:MM:SSZ - process_jsons.py: <message>
    """
    ts = datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    line = f"{ts} - process_jsons.py: {message}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as fh:
        fh.write(line)


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

if not os.path.isfile(VALID_FILES):
    log(f"missing valid file list: {VALID_FILES}")
    raise SystemExit(1)

with open(VALID_FILES, "r", encoding="utf-8") as fh:
    files = [line.strip() for line in fh if line.strip()]

log(f"processing {len(files)} file(s) from {VALID_FILES}")

# ---------- normalize one JSON ----------


def normalize_json(data):
    """
    Normalize a single JSON record into a consistent structure.
    """

    product = data.get("product")
    if not isinstance(product, dict):
        product = {}

    product_id = data.get("product_id", product.get("id"))
    name = data.get("name", product.get("name"))

    category = data.get("category")
    if category is None:
        category = "unknown"

    price_raw = data.get("price")
    try:
        price = float(price_raw)
    except (TypeError, ValueError):
        price = 0.0

    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        metadata = {}

    color = metadata.get("color")

    stock_raw = metadata.get("stock", 0)
    try:
        stock = int(float(stock_raw))
    except (TypeError, ValueError):
        stock = 0

    created_at = metadata.get("created_at")
    if created_at is None:
        created_at = metadata.get("created")

    return {
        "product_id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "color": color,
        "stock": stock,
        "created_at": created_at,
    }


# ---------- process each file ----------

for file_path in files:
    filename = os.path.basename(file_path)

    try:
        with open(file_path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        log(f"skipping {file_path}: {exc}")
        continue

    if not isinstance(data, dict):
        log(f"skipping {file_path}: root JSON value is not an object")
        continue

    cleaned_data = normalize_json(data)

    clean_path = os.path.join(CLEAN_DIR, filename)
    with open(clean_path, "w", encoding="utf-8") as fh:
        json.dump(cleaned_data, fh, indent=2)
        fh.write("\n")

    log(f"wrote cleaned JSON: {clean_path}")

    archive_path = os.path.join(ARCHIVE_DIR, filename)
    shutil.copy2(file_path, archive_path)

    log(f"archived: {file_path} -> {archive_path}")

log("Processing complete")
