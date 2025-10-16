import os
import random
import string
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

VAULT_FILE = "passwords.txt"
SAFE_PUNCT = "-_:."
CHARSET = string.ascii_letters + string.digits + SAFE_PUNCT
FERNET = None
SALT_FILE = "vault.salt"


# Base Functions
def generate_password(length: int) -> str:
    chars = random.choices(CHARSET, k=length)
    return "".join(chars)


def existing_labels(file_path: str = VAULT_FILE) -> set:
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


def upsert_entry(label: str, value: str, file_path: str = VAULT_FILE) -> None:
    lines = []
    found = False

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    continue
                key, _, _ = line.partition(":")
                if key.strip() == label:
                    lines.append(f"{label}: {value}")
                    found = True
                else:
                    lines.append(line)

    if not found:
        lines.append(f"{label}: {value}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def list_passwords(file_path: str = VAULT_FILE) -> None:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        if not lines:
            print("No entries found.")
            return
        for i, entry in enumerate(lines, 1):
            if ":" not in entry:
                print(f"{i}. {entry}")
                continue
            label, enc = entry.split(":", 1)
            token = enc.strip()
            try:
                pw = FERNET.decrypt(token.encode()).decode()
            except Exception:
                pw = token  # falls Altbestand im Klartext
            print(f"{i}. {label.strip()}: {pw}")
    except FileNotFoundError:
        print("File not found yet. No entries.")


# Actions
def create_entry() -> None:
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

    while True:
        label = input("For which service/account? ").strip()
        if label and ":" not in label:
            break
        print("Label darf nicht leer sein und kein ':' enthalten.")

    pw = generate_password(length)
    enc = FERNET.encrypt(pw.encode()).decode()

    labels = existing_labels()
    if label in labels:
        ans = input(f"'{label}' already exists. Overwrite? (y/n): ").strip().lower()
        if ans != "y":
            print("Cancelled.")
            return
        upsert_entry(label, enc)
    else:
        upsert_entry(label, enc)

    print(f"Saved under '{label}'.")
    print("Password:", pw)


# Crypto
def _salt():
    if os.path.exists(SALT_FILE):
        return open(SALT_FILE, "rb").read()
    s = os.urandom(16)
    with open(SALT_FILE, "wb") as f:
        f.write(s)
    return s


def init_crypto():
    global FERNET
    master = input("Master password: ").encode("utf-8")
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=_salt(), iterations=390_000)
    key = base64.urlsafe_b64encode(kdf.derive(master))
    FERNET = Fernet(key)


# Menu
def main() -> None:
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


if __name__ == "__main__":
    init_crypto()
    main()