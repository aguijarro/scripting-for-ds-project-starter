# Project Instructions

## Directory Structure

The project starter files contain a directory structure like this:

```
├── archive/
├── clean/
├── dataset/
├── invalid/
├── json_dump/
├── logs/
├── raw/
├── merge_to_dataset.py
├── organize_files.sh
├── process_jsons.py
├── README.md
├── run_pipeline.sh
├── valid_files.txt
├── validate_and_route.sh
└── validate_json.py
```

Your task is to transform and clean the raw data files located in the `json_dump/` directory. After multiple phases of transformation, your final files will be stored in the `dataset/` directory.

> **Do not manually move files between folders.** All file movement must be done through scripts.

> **Re-runnable by design:** Every phase clears its output directory before writing and uses `cp` (copy) instead of `mv` (move). The `json_dump/` directory is never modified. If you make a mistake in any phase, simply fix your code and run it again — you do not need to reset the starter files.

---

## Phase 0: JSON Dump (No Action Required)

The `json_dump/` directory contains the raw input files. Review the files to notice inconsistencies in filenames, casing, extensions, and JSON structures. You do **not** need to change anything in `json_dump/`.

---

## Phase 1: Filename Organization

In this phase, you will use a shell script to clean and standardize the filenames. The source is `json_dump/` and the destination is `raw/`.

To complete this phase:

1. Locate the file `organize_files.sh` in the root of your project directory
2. Within `organize_files.sh`, complete the TODO items
3. Make `organize_files.sh` executable and run it from the terminal
4. Manually inspect the `raw/` directory for your files and the `logs/` directory for your logs

For example, in `json_dump/` there was an original file named `PrOducT 001.json`. After this step, there should be a corresponding file named something like `product_001_202************Z.json` where the `*` are replaced with your specific timestamps.

In the `logs/` directory, there should be a new file named for today's date containing 44 rows of data (start, finish, plus 42 timestamped logs for the transformations of each file).

The `json_dump/` directory should be **unchanged** after running this step.

---

## Phase 2: Validation and Routing

In this phase, you will validate each JSON file in `raw/` and route the results: valid files are tracked in a list, and invalid files are copied to the `invalid/` directory.

To complete this phase:

1. Locate the file `validate_json.py` in the root of your project directory
2. Within `validate_json.py`, complete the TODO items. This script takes a single file path as a command-line argument and should exit with status code `0` if the file is valid, or a non-zero status code (e.g., `sys.exit(1)`) if it is invalid. A file is invalid if it is empty, contains broken JSON, or is missing required fields
3. Test `validate_json.py` on individual files before moving on:
   ```bash
   python3 validate_json.py raw/product_001_202************Z.json
   echo $?
   ```
   This should print `0` for a valid file and `1` for an invalid file.
4. Locate the file `validate_and_route.sh` in the root of your project directory
5. Within `validate_and_route.sh`, complete the TODO items
6. Make `validate_and_route.sh` executable and run it from the terminal
7. Manually inspect the results:
   - `valid_files.txt` should contain one file path per line, listing only valid JSON files
   - `invalid/` should contain copies of files that failed validation (empty files, broken JSON, files missing required fields)
   - The daily log file should have new entries for each validated file

---

## Phase 3: Data Cleaning

In this phase, you will normalize the JSON data from valid files into a consistent structure, write cleaned files to `clean/`, and copy the originals to `archive/`.

To complete this phase:

1. Locate the file `process_jsons.py` in the root of your project directory
2. Within `process_jsons.py`, complete the TODO items. Pay special attention to the `normalize_json()` function — the input data has two different structures (flat and nested) that need to be normalized into one consistent format
3. Run the script from the terminal: `python3 process_jsons.py`
4. Manually inspect the results:
   - Each file in `clean/` should have the same consistent set of keys (`product_id`, `name`, `category`, `price`, `color`, `stock`, `created_at`)
   - `archive/` should contain copies of the original files from `raw/` that were successfully processed
   - Open a cleaned file and compare it to the corresponding original in `json_dump/` to confirm the normalization is correct

---

## Phase 4: Dataset Creation

In this phase, you will merge all cleaned JSON files into a single CSV file using pandas.

To complete this phase:

1. Locate the file `merge_to_dataset.py` in the root of your project directory
2. Within `merge_to_dataset.py`, complete the TODO items
3. Run the script from the terminal: `python3 merge_to_dataset.py`
4. Manually inspect the results:
   - `dataset/clean_products.csv` should exist and contain one row per product
   - The CSV should have the expected columns: `product_id`, `name`, `category`, `price`, `color`, `stock`, `created_at`
   - There should be **no index column** (the first column should be `product_id`, not a row number)

---

## Phase 5: Pipeline Orchestration

In this phase, you will wire everything together so the entire pipeline runs with a single command.

To complete this phase:

1. Locate the file `run_pipeline.sh` in the root of your project directory
2. Within `run_pipeline.sh`, complete the TODO items
3. Make `run_pipeline.sh` executable and run it from the terminal
4. After running, confirm:
   - `raw/` contains normalized filenames
   - `invalid/` contains rejected files
   - `valid_files.txt` lists only valid file paths
   - `clean/` contains normalized JSON files
   - `archive/` contains copies of processed originals
   - `dataset/clean_products.csv` exists with one row per product
   - `logs/` contains a daily log file with entries from all scripts
   - The pipeline exits with code `0`

---

## Tips

### Opening the Terminal in VS Code

Click **View** > **Terminal**.

### Making Files Executable

Use the `chmod` command. For example:
```bash
chmod +x organize_files.sh
```

### Running Shell Scripts from the Terminal

Use dot-slash (`./`). For example:
```bash
./organize_files.sh
```

---

## Submitting Your Project

You can submit your completed project directly in the Udacity Workspace.

If you worked locally instead, you can submit either a zip file of your project or the URL of a public GitHub repository containing your code.

Before submitting, take a moment to review the [project rubric](Rubric.md). The rubric is your guide to what reviewers will be looking for.
