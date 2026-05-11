#!/usr/bin/env python3

import json
import os
import sys
import pandas as pd
import datetime

# ---------- logging ----------
LOGS_DIR = "logs"
TODAY = datetime.datetime.utcnow().strftime("%Y-%m-%d")
LOG_FILE = os.path.join(LOGS_DIR, f"{TODAY}.log")
os.makedirs(LOGS_DIR, exist_ok=True)


def log(message):
    """
    Write a timestamped log message to the daily log file.

    The log format should be:
    YYYY-MM-DDTHH:MM:SSZ - merge_to_dataset.py: <message>
    """
    ts = datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    line = f"{ts} - merge_to_dataset.py: {message}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as fh:
        fh.write(line)


# -----------------------------

CLEAN_DIR = "clean"
DATASET_DIR = "dataset"
OUTPUT_FILE = os.path.join(DATASET_DIR, "clean_products.csv")

COLUMNS = [
    "product_id",
    "name",
    "category",
    "price",
    "color",
    "stock",
    "created_at",
]

# Create dataset directory if it does not exist
os.makedirs(DATASET_DIR, exist_ok=True)

rows = []

log("Starting dataset merge")

for filename in sorted(os.listdir(CLEAN_DIR)):
    if not filename.endswith(".json"):
        continue

    file_path = os.path.join(CLEAN_DIR, filename)

    try:
        with open(file_path, "r", encoding="utf-8") as fh:
            row = json.load(fh)
        rows.append(row)
        log(f"loaded: {file_path}")
    except Exception as exc:
        log(f"failed to load {file_path}: {exc}")

if not rows:
    log("no rows loaded; aborting merge")
    sys.exit(1)

# ---------- pandas aggregation ----------

df = pd.DataFrame(rows)
df = df.reindex(columns=COLUMNS)

df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0.0).astype("float64")
df["stock"] = pd.to_numeric(df["stock"], errors="coerce").fillna(0).astype("int64")

df.to_csv(OUTPUT_FILE, index=False)

log(f"dataset written successfully: {OUTPUT_FILE} ({len(df)} row(s))")
log("merge process is complete")
