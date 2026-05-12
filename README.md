# Python File Data Toolkit

## Overview

**Python File Data Toolkit** is a small Python command-line project created to practice file and folder handling with `pathlib`.

The goal of this project is to consolidate the basics of working with text files in Python:

- creating folders;
- writing text files;
- reading text files;
- browsing a directory;
- filtering files by extension;
- counting lines;
- generating a text report.

This project is intentionally simple. It focuses only on Python file handling fundamentals and does not use JSON, CSV, external libraries, object-oriented programming, or automated tests yet.

---

## Project goal

The main goal is to build a clean and understandable Python script that can:

1. Create a workspace folder.
2. Generate sample files with different extensions.
3. Browse the workspace folder.
4. Read only text files.
5. Ignore unsupported file types.
6. Count the number of lines in each text file.
7. Generate a report inside a dedicated reports folder.

This project is part of a progressive learning path toward becoming more autonomous with Python and backend development.

---

## Features

The script currently supports:

- automatic creation of an `input_files/` folder;
- automatic creation of a `reports/` folder;
- generation of sample files:
  - `notes.txt`
  - `tasks.txt`
  - `readme.md`
  - `errors.log`
  - `draft.TXT`
- filtering only `.txt` files;
- support for uppercase extensions like `.TXT`;
- reading file content with UTF-8 encoding;
- counting lines with `splitlines()`;
- generating a text report in:

```text
reports/text_files_report.txt
````

---

## Project structure

```text
python-file-data-toolkit/
├── README.md
├── .gitignore
├── main.py
├── input_files/
│   ├── notes.txt
│   ├── tasks.txt
│   ├── readme.md
│   ├── errors.log
│   └── draft.TXT
└── reports/
    └── text_files_report.txt
```

The `input_files/` and `reports/` folders are created by the script when it runs.

---

## How it works

The script follows this logic:

```text
1. Create the input folder.
2. Create the reports folder.
3. Generate sample files.
4. Browse the input folder.
5. Keep only files with a .txt extension.
6. Read each accepted file.
7. Count its lines.
8. Add the result to a report.
9. Save the report into the reports folder.
10. Display the report in the terminal.
```

---

## Requirements

You only need Python installed.

Recommended version:

```text
Python 3.10+
```

No external dependency is required.

---

## How to run the project

Clone the repository:

```bash
git clone https://github.com/Jeeazy971/python-file-data-toolkit.git
```

Go into the project folder:

```bash
cd python-file-data-toolkit
```

Run the script:

```bash
python main.py
```

On some systems, you may need:

```bash
python3 main.py
```

---

## Example output

```text
Text files report
-----------------
File: notes.txt
Path: input_files/notes.txt
Lines: 3
Content:
Python notes
Pathlib is useful
Files can be read

File: tasks.txt
Path: input_files/tasks.txt
Lines: 4
Content:
Tasks
Practice pathlib
Review exceptions
Generate report

File: draft.TXT
Path: input_files/draft.TXT
Lines: 2
Content:
Draft
This uppercase extension should still be accepted

Total text files: 3
```

---

## Concepts practiced

This project practices the following Python concepts:

### File and folder handling

* `Path`
* `mkdir()`
* `exist_ok=True`
* `write_text()`
* `read_text()`
* `iterdir()`

### File checks

* `is_file()`
* `is_dir()`
* `suffix`
* `suffix.lower()`

### Basic programming logic

* variables;
* conditions;
* loops;
* counters;
* string building;
* f-strings;
* line counting with `splitlines()`.

---

## Why `pathlib`?

`pathlib` makes file and folder manipulation more readable and safer than using plain strings.

Example:

```python
report_path = reports_folder / "text_files_report.txt"
```

This is clearer than manually writing:

```python
"reports/text_files_report.txt"
```

With `pathlib`, paths become objects that can be checked, created, read from, and written to.

---

## Current limitations

This project is intentionally limited because it focuses on Python file basics.

It does not currently include:

* JSON handling;
* CSV handling;
* custom functions;
* multiple Python modules;
* object-oriented programming;
* automated tests;
* command-line arguments;
* recursive folder browsing.

These features may be added later as new Python concepts are learned.

---

## Future improvements

Possible improvements for future versions:

* split the script into functions;
* add JSON support;
* add CSV support;
* add command-line options;
* add error handling for missing folders;
* add tests with `pytest`;
* create a more advanced report format;
* support recursive folder browsing;
* allow the user to choose the folder to analyze.

---

## What I learned

By building this project, I practiced how to:

* create folders with Python;
* create and write text files;
* read text files safely;
* browse a folder;
* distinguish files from folders;
* filter files by extension;
* handle uppercase extensions;
* count lines in a file;
* generate a simple text report;
* organize a small Python project for a portfolio.

---

## Author

Created as part of a personal Python learning roadmap focused on building solid programming foundations and becoming more autonomous as a developer.

