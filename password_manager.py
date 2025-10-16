import os
import random
import string

VAULT_FILE = "passwords.txt"
SAFE_PUNCT = "-_:."
CHARSET = string.ascii_letters + string.digits + SAFE_PUNCT


# Base Functions
def generate_password(length: int) -> str:
    """Generate a random password with the specified length."""
    chars = random.choices(CHARSET, k=length)
    return "".join(chars)


def existing_labels(file_path: str = VAULT_FILE) -> set:
    """Get a set of all existing labels from the vault file."""
    if not os.path.exists(file_path):
        return set()
    labels = set()
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            label = line.split(":", 1)[0].strip()
            labels.add(label)
    return labels


def upsert_entry(label: str, pw: str, file_path: str = VAULT_FILE) -> None:
    """Replace existing label entry or append new one."""
    lines = []
    found = False

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                key, _, _ = line.partition(":")
                if key.strip() == label:
                    lines.append(f"{label}: {pw}")
                    found = True
                else:
                    lines.append(line)

    if not found:
        lines.append(f"{label}: {pw}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def list_passwords(file_path: str = VAULT_FILE) -> None:
    """Display all saved passwords from the vault file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        if not lines:
            print("No entries found.")
            return
        for i, entry in enumerate(lines, 1):
            print(f"{i}. {entry}")
    except FileNotFoundError:
        print("File not found yet. No entries.")


# Actions 
def create_entry() -> None:
    """Create a new password entry with validation."""
    while True: 
         s = input("Password length: ").strip()
         try:
             length = int(s)
             if length < 1:
                 print("Please enter a number ≥ 1.")
                 continue
            
             break 
         except ValueError:
              print("That's not a number. Please try again.")
         

    label = input("For which service/account? ").strip()
    pw = generate_password(length)

    labels = existing_labels()
    if label in labels:
        ans = input(f"'{label}' already exists. Overwrite? (y/n): ").strip().lower()
        if ans != "y":
            print("Cancelled.")
            return
        upsert_entry(label, pw)
    else:
        with open(VAULT_FILE, "a", encoding="utf-8") as f:
            f.write(f"{label}: {pw}\n")

    print(f"Saved under '{label}'.")
    print("Password:", pw)


# Menu
def main() -> None:
    """Main program loop with menu options."""
    while True:
        print("\n[1] Create new  [2] Show all  [0] Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            create_entry()
        elif choice == "2":
            list_passwords()
        elif choice == "0":
            print("Bye.")
            break
        else:
            print("Invalid choice.")

main()