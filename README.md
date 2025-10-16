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
**Secure** command-line based password manager with encryption:
- **🔒 Encryption**: Passwords are encrypted using Fernet (symmetric encryption) before storage
- **🔑 Master Password**: Protected by a master password with PBKDF2 key derivation (390,000 iterations)
- **Password Generation**: Secure, random passwords with configurable length
- **Input Validation**: Ensures password length is ≥ 1 and labels don't contain ':'
- **Duplicate Detection**: Checks for existing labels and prompts for overwrite confirmation
- **Upsert Functionality**: Updates existing entries or creates new ones seamlessly
- **Storage**: Encrypted storage in `passwords.txt` with UTF-8 encoding
- **Salt Management**: Automatic salt generation and persistence in `vault.salt`
- **Character Set**: Letters, numbers, and safe special characters (`-_:.`)
- **Type Hints**: Fully typed functions for better code quality

**Menu Options:**
- [1] Create new entry (with duplicate check, validation, and encryption)
- [2] Show all passwords (decrypted display)
- [0] Exit program

**Security Features:**
- 🛡️ **Master Password Protection**: Required on startup to unlock the vault
- 🔐 **PBKDF2 Key Derivation**: 390,000 iterations with SHA-256
- 🔒 **Fernet Encryption**: Industry-standard symmetric encryption
- 🧂 **Persistent Salt**: Unique salt stored in `vault.salt`
- ✅ **Automatic Decryption**: Passwords decrypted only when displayed
- 🔄 **Backwards Compatible**: Handles legacy plaintext entries gracefully

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
- **cryptography** library (for password encryption)

### Setup
```bash
# Clone the repository
git clone https://github.com/eduart-maliqi/learn-How-To-Automate-Python.git

# Navigate to the project directory
cd learn-How-To-Automate-Python

# Install required dependencies
pip install cryptography
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

**🔒 First Run:**
1. You'll be prompted to create a **master password**
2. A unique salt file (`vault.salt`) will be generated automatically
3. This master password will be required every time you use the password manager

**Usage:**
- **Master Password**: Enter your master password to unlock the vault
- **Create Password**: Choose option `[1]` to generate and save a new encrypted password
- **View Passwords**: Choose option `[2]` to see all passwords (automatically decrypted)
- **Exit**: Choose option `[0]` to close the program

**Enhanced Features:**
- **🔐 Encryption**: All passwords are encrypted with Fernet before storage
- **🔑 Master Password**: PBKDF2 key derivation with 390,000 iterations
- **Duplicate Detection**: Asks for confirmation before overwriting existing entries
- **Input Validation**: Ensures password length ≥ 1 and labels don't contain ':'
- **Backwards Compatibility**: Can read old plaintext passwords if any exist

**Example Workflow:**
1. Run the program and enter your master password
2. Choose option `[1]` to create a new password
3. Enter desired password length (minimum 1, recommended 12+)
4. Enter a label/service name (e.g., "GitHub", "Gmail")
5. If the label exists, confirm whether to overwrite
6. Your encrypted password is saved and the plaintext is displayed once

**⚠️ Important:**
- Remember your master password! It cannot be recovered if lost
- The `vault.salt` file is crucial - back it up along with `passwords.txt`
- Losing either file means you cannot decrypt your passwords

### Password Manager (GUI)
```bash
python password_gui.py
```
The graphical interface opens automatically.

**Tips:**
- Minimum length: 1 character (recommended: 12+ characters for security)
- CLI passwords are **encrypted** and require master password
- Passwords are saved in `passwords.txt` (encrypted format)
- GUI passwords are saved in plaintext (GUI version has no encryption yet)
- Use the copy function in GUI for easy pasting
- CLI prevents accidental overwrites with confirmation prompts
- **Back up both** `passwords.txt` and `vault.salt` to prevent data loss

## 📂 Project Structure

```
learn-How-To-Automate-Python/
│
├── File-organizer.py               # Automatic file organization
├── password_manager.py              # CLI Password Manager (encrypted with Fernet)
├── password_gui.py                  # GUI Password Manager (plaintext)
├── passwords.txt                    # Encrypted passwords (CLI) or plaintext (GUI)
├── vault.salt                       # Salt for encryption (generated on first run)
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
- **cryptography**: Fernet encryption and PBKDF2 key derivation
- **os & shutil**: File system operations
- **tkinter**: GUI framework (Python Standard Library)
- **random & string**: Secure password generation
- **base64**: Encoding for encryption keys

## 🔮 Future Enhancements

- [ ] Add encryption to GUI password manager
- [ ] Configuration file for File Organizer
- [ ] Undo function for file organization
- [ ] Password strength analysis and visual indicator
- [ ] Search function in Password Manager
- [ ] Export/Import of passwords (CSV/JSON)
- [ ] Integration of AI features
- [ ] Password change history/versioning
- [ ] Two-factor authentication option
- [x] **Encryption for stored passwords** ✅
- [x] Duplicate label detection with overwrite confirmation
- [x] Input validation for password length
- [x] Type hints for better code maintainability
- [x] Master password protection with PBKDF2

## ⚠️ Security Notice

**CLI Password Manager:** Passwords are now **encrypted** using industry-standard Fernet encryption with PBKDF2 key derivation (390,000 iterations). Your master password protects all stored passwords. 

**Important:**
- 🔑 **Remember your master password** - it cannot be recovered if lost
- 💾 **Back up `vault.salt` and `passwords.txt`** - both are needed to decrypt passwords
- 🔒 **Keep your master password secure** - anyone with it can decrypt all passwords
- ⚠️ **GUI version still uses plaintext** - encryption not yet implemented in GUI

**Note:** While the CLI now offers strong encryption, this project is still primarily for learning purposes. For critical production use, consider established password managers with additional security features like clipboard clearing, timeout locks, and secure memory handling.

## 📝 License

This project is for learning and educational purposes.

## 👨‍💻 Author

**eduart-maliqi**

---

*Learn Python automation through practical examples! 🚀*
