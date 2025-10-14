import os
import shutil

# Pfad zum Test-Ordner
source_folder = "test_files"

# Unterordner für die Sortierung
folders = {
    "Bilder": [".jpg", ".png", ".jpeg"],
    "Dokumente": [".pdf", ".docx", ".txt"],
    "Musik": [".mp3", ".wav", ".mp4"],
    "Programme": [".exe"],
}

print("Ordnerstruktur:", folders)  # Debug-Ausgabe

# 1️⃣ Alle Dateien im Test-Ordner durchgehen
for filename in os.listdir(source_folder):
    filepath = os.path.join(source_folder, filename)

    # Überspringen, wenn es ein Ordner ist
    if os.path.isdir(filepath):
        continue

    # Jede echte Datei anzeigen
    print(filename, "→", os.path.splitext(filename)[1].lower())

    # 2️⃣ Dateiendung prüfen und verschieben
    file_ext = os.path.splitext(filename)[1].lower()
    moved = False

    for folder_name, extensions in folders.items():
        if file_ext in extensions:
            target_folder = os.path.join(source_folder, folder_name)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(target_folder, filename))
            print(f"Verschoben: {filename} → {folder_name}")
            moved = True
            break

    # Falls die Endung keiner Kategorie entspricht
    if not moved:
        other_folder = os.path.join(source_folder, "Sonstiges")
        os.makedirs(other_folder, exist_ok=True)
        shutil.move(filepath, os.path.join(other_folder, filename))
        print(f"Verschoben: {filename} → Sonstiges")
