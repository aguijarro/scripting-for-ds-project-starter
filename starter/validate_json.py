#!/usr/bin/env python3

import json
import sys
import os
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
    YYYY-MM-DDTHH:MM:SSZ - validate_json.py: <message>
    """
    ts = datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    line = f"{ts} - validate_json.py: {message}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as fh:
        fh.write(line)


# -----------------------------


def main():
    if len(sys.argv) != 2:
        log("expected exactly one command-line argument (file path)")
        sys.exit(1)

    path = sys.argv[1]

    try:
        with open(path, "r", encoding="utf-8") as fh:
            raw = fh.read()
    except OSError as exc:
        log(f"cannot read file {path}: {exc}")
        sys.exit(1)

    if raw.strip() == "":
        log(f"empty file: {path}")
        sys.exit(1)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        log(f"invalid JSON in {path}: {exc}")
        sys.exit(1)

    if not isinstance(data, dict):
        log(f"JSON root must be an object (dict): {path}")
        sys.exit(1)

    product = data.get("product")
    if not isinstance(product, dict):
        product = {}

    product_id = data.get("product_id", product.get("id"))
    name = data.get("name", product.get("name"))
    price = data.get("price")
    metadata = data.get("metadata")

    if product_id is None:
        log(f"missing product identifier (product_id or product.id): {path}")
        sys.exit(1)
    if name is None:
        log(f"missing product name (name or product.name): {path}")
        sys.exit(1)
    if price is None:
        log(f"missing price: {path}")
        sys.exit(1)
    if not isinstance(metadata, dict):
        log(f"missing or invalid metadata object: {path}")
        sys.exit(1)
    if "color" not in metadata:
        log(f"missing required field metadata.color: {path}")
        sys.exit(1)
    if "stock" not in metadata:
        log(f"missing required field metadata.stock: {path}")
        sys.exit(1)
    if "created_at" not in metadata and "created" not in metadata:
        log(
            f"missing required timestamp metadata.created_at or metadata.created: {path}"
        )
        sys.exit(1)

    log(f"valid JSON: {path}")
    sys.exit(0)


if __name__ == "__main__":
    main()
