# Basic Antivirus Scanner

A beginner-friendly Python project that scans files in the `sample_files` folder for predefined **demonstration signatures**.

> **Safety and accuracy note:** The signatures in this repository are invented test strings, not real malware signatures. A clean result does not prove a file is safe. This project is for learning and is not a replacement for Microsoft Defender or another reputable antivirus product.

## Features

- Scans files in a sample folder.
- Checks file content against two demonstration signatures.
- Prints an alert when a test marker is found.
- Handles file-reading errors.
- Displays a simple scan summary.
- Includes sample files, automated tests, and interview preparation.

## Requirements

- Python 3.9 or newer recommended.
- No third-party packages are required.

## Run the scanner

Open a terminal in the project folder and run:

```bash
python main.py
```

## Test it

Run the automated tests:

```bash
python -m unittest discover -s tests -v
```

To test manually, add the text `DEMO_MALWARE_MARKER` to a new file in `sample_files`, save it, and run the scanner again.

## Project structure

```text
basic-antivirus/
│
├── main.py
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── sample_files/
│   ├── clean.txt
│   └── test_marker.txt
│
└── tests/
    └── test_scanner.py
```

## How it works

1. The program lists files in `sample_files`.
2. It opens each file in binary mode.
3. It checks whether any predefined test signature occurs in the file.
4. It prints an alert or a clean result.
5. It displays the number of files scanned and matches found.

## Limitations

- Uses invented demonstration strings only.
- Does not detect real malware reliably.
- Does not use a commercial antivirus engine or malware database.
- Does not delete, quarantine, or modify files.
- Does not continuously monitor the computer.

## Resume description

**Basic Antivirus Scanner | Python**

Created a beginner-level Python scanner that checks sample files for predefined demonstration patterns, reports matches, handles file-reading errors, and summarizes scan results.

