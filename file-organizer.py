import os
from pathlib import Path

# Map each folder name to the extensions that belong in it
FILE_TYPES = {
    "Application":[".exe"],
    "Document": ['doc', 'docx', 'odt', 'pdf', 'xls', 'xlsx', 'ods', 'ppt', 'pptx'],
    "Excel":[".xls", ".xlsx", ".csv"],
    "Icons":[".ico"],
    "Music": [".mp3", ".msv", ".wav", ".wma"],
    "Picture": [".jpeg", ".jpg", ".png", ".gif"],
    "SQL":[".sql"],
    "Video": [".wmv", ".mov", ".mp4", ".mpg", ".mpeg", ".mkv"],
    "Zip": [".zip", ".iso", ".tar"]
}

EXTENSION_TO_FOLDER = {
    extension: folder
    for folder, extensions in FILE_TYPES.items()
    for extension in extensions
}

# This is the folder that gets to be organized, TARGET_DIR = Path("D:/MyFolder")
TARGET_DIR = Path.home() / "Downloads"

def organizer(target_dir: Path):
    """Sort every file in target_dir into subfolders by file type."""
    for entry in os.scandir(target_dir):
        if entry.is_dir():
            continue

        file_path = Path(entry.path)
        extension = file_path.suffix.lower()

        folder_name = EXTENSION_TO_FOLDER.get(extension, "Other_Folder")
        destination_dir = target_dir / folder_name

        destination_dir.mkdir(exist_ok=True)
        destination_path = destination_dir / file_path.name

        try:
            file_path.rename(destination_path)
            print(f"Moved {file_path.name} -> {folder_name}/")
        except FileExistsError:
            print(f"Skipped {file_path.name}: already exists in {folder_name}/")


if __name__ == "__main__":
    organizer(TARGET_DIR)