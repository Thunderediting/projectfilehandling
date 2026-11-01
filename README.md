# Personal Journal Manager

A lightweight, menu-driven Python application for recording personal journal entries in a local text file. It gives users a straightforward way to add timestamped notes and review saved entries from the command line.

## Project Overview

The Personal Journal Manager is a beginner-friendly file-handling project that demonstrates how a Python script can collect user input, work with dates and times, and store text locally. Entries are saved in `data.txt`, so they remain available between runs without requiring a database or external service.

## Highlights

- Add a journal entry with its creation date and time.
- Display saved entries through an interactive command-line menu.
- Store journal data locally in a plain-text file.
- Use Python's standard library for date/time handling and file operations.

## Run the Project

From the project directory, run:

```bash
python projectfilehanding.py
```

The application will display a menu in the terminal. Journal data is stored in `data.txt` in the current working directory.

## Technology

- Python
- Standard library: `datetime` and `os`
- Plain-text file storage

## Project Status

This project is an early command-line prototype. Search and deletion options are present in the menu but are not yet fully implemented.
