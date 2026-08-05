# week1-foundations - Python Environment Setup and Basic Program

## Overview

This lab focuses on setting up a Python development environment using a virtual environment (`venv`) and creating a basic Python program. It demonstrates the standard project structure used in Python development and introduces essential tools required for managing Python projects.

---

## Objective

The objectives of this lab are:

- Set up a Python development environment in Ubuntu (WSL).
- Create and activate a Python virtual environment.
- Create a basic Python application.
- Display the user's name and the current Python version.
- Create essential project files.
- Understand basic project organization and dependency management.

---

## Technologies and Tools Used

- Ubuntu (WSL2)
- Python 3
- Python Virtual Environment (`venv`)
- pip
- Nano Text Editor
- Git (Project Version Control)

---

## Project Structure

```text
week1-foundations/
│
├── .venv/
├── .gitignore
├── README.md
├── requirements.txt
└── hello.py
```

---

## Source Code

### hello.py

```python
import sys

# Lab 1:
# Create a Python program that prints my name and
# displays the Python version currently being used.

def main():
    # Print my name
    print("Name: Gursimar")

    # Print the Python interpreter version
    print(f"Python Version: {sys.version}")



```

---

## Code Explanation

### Import Statement

```python
import sys
```

Imports Python's built-in `sys` module, which provides information about the Python interpreter.

---

### main() Function

```python
def main():
```

Defines the main function of the program. All program logic is placed inside this function for better organization and maintainability.

---

### Printing the Name

```python
print("Name: Gursimar")
```

Displays the user's name on the terminal.

---

### Printing the Python Version

```python
print(f"Python Version: {sys.version}")
```

Uses an f-string to display the Python interpreter version stored in `sys.version`.

---


## How to Run the Program

### Activate the Virtual Environment

```bash
source .venv/bin/activate
```

### Execute the Program

```bash
python hello.py
```

---

## Expected Output

```text
Name: Gursimar
Python Version: 3.x.x
```

(The version number depends on the installed Python version.)

---

## Problems Faced

### Problem 1

**Issue**

The `wsl` command launched Docker Desktop instead of Ubuntu.

**Cause**

Docker Desktop was configured as the default WSL distribution.

**Solution**

Changed the default WSL distribution to Ubuntu using:

```bash
wsl --set-default Ubuntu
```

---

### Problem 2

**Issue**

`python3` command was not found.

**Cause**

The Docker Desktop environment was being used instead of Ubuntu.

**Solution**

Switched to the Ubuntu WSL distribution.

---

### Problem 3

**Issue**

Permission denied while creating the virtual environment.

**Cause**

The project directory was previously created by the root user.

**Solution**

Removed the root-owned directory and recreated it using the normal Ubuntu user.

---

### Problem 4

**Issue**

Virtual environment creation failed because `python3-venv` was missing.

**Cause**

The required package was not installed.

**Solution**

Installed the required packages using:

```bash
sudo apt update
sudo apt install python3-venv python3-pip
```

---

## Learning Outcomes

Through this lab, I learned how to:

- Navigate Linux using the terminal.
- Create and activate Python virtual environments.
- Organize a Python project.
- Use Nano to edit files.
- Understand the purpose of `venv`.
- Use Python modules such as `sys`.
- Work with f-strings.
- Troubleshoot common WSL and Python setup issues.

---

## Author

**Name:** Gursimar

**Lab:** Python Lab 01

**Environment:** Ubuntu (WSL2)
