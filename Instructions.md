Directory Structure
The project starter files contain a directory structure like this:
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
Your task is to transform and clean the raw data files located in the json_dump/ directory. After multiple phases of transformation, your final files will be stored in the dataset/ directory.
⚠️ Do not manually move files between folders. All file movement must be done through scripts.

Phase 0: JSON Dump
Phase 0 is the initial state of the starter files. You do not need to make any changes to the files in the json_dump/ directory. However, you may want to review the files to note the inconsistencies and messy file names.

Phase 1: Filename Organization
In this phase, you will use a shell script to clean and standardize the file names. The source for this step is the json_dump/ directory, and the destination is the raw/ directory. Your script will also log when it starts and finishes, along with an entry for each file.
To complete this phase:
Locate the file organize_files.sh in the root of your project directory
Within organize_files.sh, complete the TODO items
Make organize_files.sh executable and run it from the terminal
Manually inspect the raw/ directory for your files and the logs/ directory for your logs
For example, in json_dump/ there was an original file named PrOducT 001.json. After this step, there should be a corresponding file named something like product_001_202************Z.json where the * are replaced with your specific timestamps.
In the logs/ directory, there should be a new file named for today's date containing 44 rows of data (start, finish, plus 42 timestamped logs for the transformations of each file)

Phase 2: Validation and Routing
In this phase, you will use a shell script and a Python script to determine whether the files under raw/ are valid JSON files, and move the invalid files to the invalid/ directory.

Tips
Opening the Terminal in VS Code
Click View → Terminal
Making Files Executable
Use the chmod command. For example:
chmod +x organize_files.sh
Running Shell Scripts from the Terminal
Use dot-slash (./). For example:
./organize_files.sh


You are expected to complete the following deliverables:
Filename Organization
  Implement logic in organize_files.sh to normalize filenames and move files into the raw/ folder.
Validation and Routing
Implement validate_json.py to determine whether a JSON file is valid.
Implement validate_and_route.sh to:
Validate files in raw/
Move invalid files to invalid/
Track valid files in valid_files.txt
Data Cleaning
Implement process_jsons.py to:
Normalize different JSON structures into a consistent format
Write cleaned JSON files to the clean/ folder
Dataset Creation
Implement merge_to_dataset.py to:
Read all cleaned JSON files
Merge them into a single CSV dataset using pandas
Save the dataset to the dataset/ folder
  Archive original files after successful processing
Pipeline Execution
Implement run_pipeline.sh so the entire pipeline can be executed with a single command.
Do not manually move files between folders.
All file movement must be done through scripts.
Project Folder Structure and Pipeline Phases
json_dump/ — Phase 0: Incoming data
Raw input files as received. Filenames and data may be inconsistent.
raw/ — Phase 1: Organized files
Files after filename normalization. Contents are unchanged.
invalid/ — Phase 2: Rejected data
Files that failed validation and are excluded from processing.
clean/ — Phase 3: Normalized data
Files with standardized and consistent structure.
archive/ — Phase 4: Archived originals
Original files that were successfully processed and archived.
dataset/ — Phase 5: Final dataset
Aggregated dataset ready for analysis or machine learning.
logs/ — Cross-cutting: Pipeline logs
Execution logs for all pipeline steps.
Built With
Python – Core scripting language for validation and processing
pandas – Used to merge cleaned data into a final dataset
Bash – Used for file automation and orchestration
Unix shell utilities – Standard tools for file navigation and scripting


Submitting Your Project
You can submit your completed project directly in the Udacity Workspace.
If you worked locally instead, you can submit either a zip file of your project or the URL of a public GitHub repository containing your code.  
Before submitting, take a moment to review the project rubric. The rubric is your guide to what reviewers will be looking for.