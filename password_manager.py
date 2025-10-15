import random
import string
SAFE_PUNCT = "-_:."
VAULT_FILE = "passwoerter.txt"
CHARSET = string.ascii_letters + string.digits + SAFE_PUNCT



def generate_password(length):
    chars = random.choices(CHARSET, k=length)
    return "".join(chars)

def create_entry():
    # Eingaben
    length = int(input("Passwortlänge: "))
    label = input("Für welchen Dienst/Account? ").strip()

    # Passwort erzeugen
    pw = generate_password(length)

    # Speichern (anhängen)
    with open(VAULT_FILE, "a", encoding="utf-8") as f:
        f.write(f"{label}: {pw}\n")

  
    print(f"Gespeichert unter '{label}'.")
    print("Passwort:", pw)

def list_passwords(file_path=VAULT_FILE):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        if not lines:
            print("Keine Einträge.")
            return
        for i, entry in enumerate(lines, 1):
            print(f"{i}. {entry}")
    except FileNotFoundError:
        print("Datei noch nicht vorhanden. Keine Einträge.")

def main():
    while True:
        print("\n[1] Neu anlegen  [2] Anzeigen  [0] Beenden")
        choice = input("Auswahl: ").strip()

        if choice == "1":
            create_entry()
        elif choice == "2":
            list_passwords()
        elif choice == "0":
            print("Bye.")
            break
        else:
            print("Ungültig.")



if __name__ == "__main__":
    main()





