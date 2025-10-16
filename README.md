# 🐍 Python Automation Learning Project

A practical learning project for automating everyday tasks with Python. This repository contains various useful tools for file organization and password management.

## 📋 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Technologies](#-technologies)
- [Future Enhancements](#-future-enhancements)

## ✨ Features

### 1. 📁 File Organizer (`File-organizer.py`)
Automatic file sorting by categories:
- **Images**: `.jpg`, `.png`, `.jpeg`
- **Documents**: `.pdf`, `.docx`, `.txt`
- **Music**: `.mp3`, `.wav`, `.mp4`
- **Programs**: `.exe`
- **Other**: All other file types

**How it works:**
- Scans a specified folder for files
- Automatically creates subfolders for each category
- Moves files based on their extension
- Uncategorized files go to the "Sonstiges" (Other) folder

### 2. 🔐 Password Manager (`password_manager.py`)
Enhanced command-line based password manager with advanced features:
- **Password Generation**: Secure, random passwords with configurable length
- **Input Validation**: Ensures password length is ≥ 1 with user-friendly error messages
- **Duplicate Detection**: Checks for existing labels and prompts for overwrite confirmation
- **Upsert Functionality**: Updates existing entries or creates new ones seamlessly
- **Storage**: Local storage in `passwords.txt` with UTF-8 encoding
- **Character Set**: Letters, numbers, and safe special characters (`-_:.`)
- **Type Hints**: Fully typed functions for better code quality

**Menu Options:**
- [1] Create new entry (with duplicate check and validation)
- [2] Show all passwords
- [0] Exit program

**Key Features:**
- Smart duplicate handling - warns before overwriting existing entries
- Robust input validation for password length
- Clean code structure with docstrings
- Error handling for missing files

### 3. 🖥️ Password Manager GUI (`password_gui.py`)
Graphical user interface for the password manager using Tkinter:
- **User-friendly interface** with intuitive input fields
- **Generate**: Creates secure passwords with desired length
- **Save**: Stores passwords with label/account names
- **Show All**: Displays all saved entries in a separate window
- **Copy**: Copies generated passwords directly to clipboard
- **Extended special characters**: `-_:;.,/`

*Note: The GUI was generated using AI assistance, with the main focus being on backend logic and functionality rather than frontend design.*

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- No additional libraries required (uses only standard modules)

### Setup
```bash
# Clone the repository
git clone https://github.com/eduart-maliqi/learn-How-To-Automate-Python.git

# Navigate to the project directory
cd learn-How-To-Automate-Python
```

## 💻 Usage

### File Organizer
```bash
python File-organizer.py
```
The script automatically organizes all files in the `test_files` folder.

**Customization:**
- Change the `source_folder` variable to organize a different folder
- Adjust the `folders` dictionary to add your own categories

### Password Manager (CLI)
```bash
python password_manager.py
```
Follow the menu instructions for password management.

**Enhanced Features:**
- **Duplicate Detection**: The manager checks if a label already exists and asks for confirmation before overwriting
- **Input Validation**: Ensures password length is at least 1 character
- **Smart Storage**: Uses `passwords.txt` for persistent storage
- **Error Messages**: Clear, user-friendly feedback for invalid inputs

**Example Usage:**
1. Choose option `[1]` to create a new password
2. Enter desired password length (minimum 1)
3. Enter a label/service name
4. If the label exists, choose whether to overwrite (y/n)
5. Your generated password will be displayed and saved

### Password Manager (GUI)
```bash
python password_gui.py
```
The graphical interface opens automatically.

**Tips:**
- Minimum length: 1 character (recommended: 12+ characters for security)
- Passwords are saved in `passwords.txt` (updated from previous version)
- Use the copy function in GUI for easy pasting
- CLI prevents accidental overwrites with confirmation prompts

## 📂 Project Structure

```
learn-How-To-Automate-Python/
│
├── File-organizer.py               # Automatic file organization
├── password_manager.py              # CLI Password Manager (with duplicate detection)
├── password_gui.py                  # GUI Password Manager
├── passwords.txt                    # Saved passwords (created automatically)
├── python_os_shutil_notes.txt      # Notes on os/shutil modules
├── password_manager_cli_notes.txt  # Notes on CLI password manager concepts
├── README.md                        # This file
│
└── test_files/                      # Test folder for File Organizer
    ├── Bilder/
    ├── Dokumente/
    ├── Musik/
    └── Sonstiges/
```

## 🛠️ Technologies

- **Python 3**: Main programming language with type hints
- **os & shutil**: File system operations
- **tkinter**: GUI framework (Python Standard Library)
- **random & string**: Secure password generation

## 🔮 Future Enhancements

- [ ] Encryption for stored passwords
- [ ] Configuration file for File Organizer
- [ ] Undo function for file organization
- [ ] Password strength analysis
- [ ] Search function in Password Manager
- [ ] Integration of AI features
- [x] Duplicate label detection with overwrite confirmation
- [x] Input validation for password length
- [x] Type hints for better code maintainability

## ⚠️ Security Notice

**Important:** Passwords are currently stored as plain text. For production use, encryption should be implemented. These tools are designed for learning purposes.

## 📝 License

This project is for learning and educational purposes.

## 👨‍💻 Author

**eduart-maliqi**

---

*Learn Python automation through practical examples! 🚀*
