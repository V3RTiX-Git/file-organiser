import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".ts", ".json"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
}

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Other"

def organise_folder(folder_path):
    if not os.path.exists(folder_path):
        return {"error": "Folder path does not exist."}

    results = {}
    skipped = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders and hidden files
        if os.path.isdir(file_path) or filename.startswith("."):
            continue

        _, ext = os.path.splitext(filename)
        if not ext:
            skipped.append(filename)
            continue

        category = get_category(ext)
        target_dir = os.path.join(folder_path, category)
        os.makedirs(target_dir, exist_ok=True)

        target_path = os.path.join(target_dir, filename)

        # Avoid overwriting files with the same name
        if os.path.exists(target_path):
            base, extension = os.path.splitext(filename)
            target_path = os.path.join(target_dir, f"{base}_copy{extension}")

        shutil.move(file_path, target_path)
        results.setdefault(category, []).append(filename)

    return {"organised": results, "skipped": skipped}