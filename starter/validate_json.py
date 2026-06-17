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


def get_merged_view(data):
    """Merge top-level fields with nested product fields for validation."""
    merged = dict(data)
    product = data.get("product")
    if isinstance(product, dict):
        for key, value in product.items():
            if key not in merged:
                merged[key] = value
    return merged


def has_required_fields(data):
    """Return True when all required product fields are present."""
    product_id = data.get("product_id", data.get("id"))
    name = data.get("name")
    price = data.get("price")
    metadata = data.get("metadata")

    if product_id is None or name is None or price is None:
        return False
    if not isinstance(metadata, dict):
        return False
    if "color" not in metadata or "stock" not in metadata:
        return False
    if "created_at" not in metadata and "created" not in metadata:
        return False
    return True


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

    if not has_required_fields(get_merged_view(data)):
        log(f"missing required fields: {path}")
        sys.exit(1)

    log(f"valid JSON: {path}")
    sys.exit(0)


if __name__ == "__main__":
    main()
