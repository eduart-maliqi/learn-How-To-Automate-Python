import random
import string
VAULT_FILE = "passwoerter.txt"


CHARSET = string.ascii_letters + string.digits + string.punctuation
user_length = int(input("Passwortlänge: "))
label = input("Für welchen Dienst/Account? ").strip()




def generate_password(length: int):
    chars = random.choices(CHARSET, k=length)
    return "".join(chars)

pw = generate_password(user_length)


with open(VAULT_FILE, "a", encoding="utf-8") as f:
    f.write(f"{label}: {pw}\n")
print(f"Gespeichert unter '{label}'.")
print("Passwort:", pw)





