import tkinter as tk
from tkinter import ttk, messagebox
import random, string, os

# ---------- Konfiguration ----------
VAULT_FILE = "passwoerter.txt"
SAFE_PUNCT = "-_:;.,/"  # nur diese Sonderzeichen zulassen
CHARSET = string.ascii_letters + string.digits + SAFE_PUNCT

# ---------- Logik ----------
def generate_password(length: int):
    chars = random.choices(CHARSET, k=length)
    return "".join(chars)

def save_entry(label: str, pw: str, file_path=VAULT_FILE):
    label = label.strip()
    if not label or not pw:
        return False
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"{label}: {pw}\n")
    return True

def read_entries(file_path=VAULT_FILE):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# ---------- GUI ----------
root = tk.Tk()
root.title("Password Manager (Mini)")
root.resizable(False, False)

length_var = tk.StringVar(value="12")
label_var  = tk.StringVar()
pw_var     = tk.StringVar()

frm = ttk.Frame(root, padding=12)
frm.grid()

# Eingaben
ttk.Label(frm, text="Länge:").grid(column=0, row=0, sticky="w")
ttk.Entry(frm, textvariable=length_var, width=8).grid(column=1, row=0, sticky="w")

ttk.Label(frm, text="Label/Account:").grid(column=0, row=1, sticky="w")
ttk.Entry(frm, textvariable=label_var, width=28).grid(column=1, row=1, sticky="w")

ttk.Label(frm, text="Passwort:").grid(column=0, row=2, sticky="w")
pw_entry = ttk.Entry(frm, textvariable=pw_var, width=32)
pw_entry.grid(column=1, row=2, sticky="w")

# Aktionen
def on_generate():
    try:
        n = int(length_var.get())
        if n < 4:
            messagebox.showwarning("Hinweis", "Bitte mindestens 4 Zeichen.")
            return
    except ValueError:
        messagebox.showerror("Fehler", "Bitte eine Zahl für die Länge eingeben.")
        return
    pw_var.set(generate_password(n))

def on_save():
    if save_entry(label_var.get(), pw_var.get()):
        messagebox.showinfo("Gespeichert", f"Eintrag '{label_var.get().strip()}' gespeichert.")
    else:
        messagebox.showwarning("Hinweis", "Label oder Passwort fehlt.")

def on_show_all():
    entries = read_entries()
    if not entries:
        messagebox.showinfo("Einträge", "Keine Einträge vorhanden.")
        return
    # Einfaches Anzeige-Fenster
    top = tk.Toplevel(root)
    top.title("Gespeicherte Einträge")
    top.resizable(True, True)
    txt = tk.Text(top, width=50, height=15)
    txt.pack(padx=8, pady=8)
    for i, line in enumerate(entries, 1):
        txt.insert("end", f"{i}. {line}\n")
    txt.config(state="disabled")

def on_copy():
    pw = pw_var.get()
    if not pw:
        messagebox.showwarning("Hinweis", "Kein Passwort zum Kopieren.")
        return
    root.clipboard_clear()
    root.clipboard_append(pw)
    messagebox.showinfo("Kopiert", "Passwort in Zwischenablage.")

btn_row = ttk.Frame(frm)
btn_row.grid(column=0, row=3, columnspan=2, pady=10, sticky="w")

ttk.Button(btn_row, text="Generieren", command=on_generate).grid(column=0, row=0, padx=(0,6))
ttk.Button(btn_row, text="Speichern",  command=on_save).grid(column=1, row=0, padx=(0,6))
ttk.Button(btn_row, text="Alle anzeigen", command=on_show_all).grid(column=2, row=0, padx=(0,6))
ttk.Button(btn_row, text="Kopieren", command=on_copy).grid(column=3, row=0)

root.mainloop()
