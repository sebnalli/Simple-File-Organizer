from pathlib import Path

images = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
documents = [".pdf", ".txt", ".doc", ".docx", ".ppt", ".pptx"]
code = [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"]
audio = [".mp3", ".wav", ".aac", ".flac", ".m4a"]
video = [".mp4", ".mov", ".avi", ".mkv", ".webm"]
archives = [".zip", ".rar", ".7z", ".tar", ".gz"]
executables = [".exe", ".msi", ".app", ".dmg", ".pkg"]

def get_folder_path():
    """Prompts user for name of path. Handles empty path input."""
    while True:
        user_input = input("\nPlease enter the path to your folder: ")
        if not user_input:
            print("\nCannot enter empty path!\n")
            continue

        folder_path = Path(user_input)
        break

    return folder_path

def validate_folder(folder_path):
    """Validates that the path exists and leads to a folder"""
    if not folder_path.exists():
        print("\nFolder does not exist!\n")
        return False

    if not folder_path.is_dir():
        print("\nThis path does not lead to a folder!\n")
        return False
    
    print("\nLocated your folder!\n")
    return True

def scan_files(folder_path):
    """Loops through the folder. Runs check for valid files. Appends valid files to a list."""
    files = []

    for item in folder_path.iterdir():
        if item.is_file():
            files.append(item)
        
    return files

def display_files(files):
    """Displays all file names and file sizes"""
    if not files:
        print("\nThis folder is empty!\n")
        return

    for file in files:
        print(f"{file.name} | {file.stat().st_size}")

def count_extensions(files):
    """Counts files by category based on their file extensions."""
    category_counts = {
        "Images": 0,
        "Documents": 0,
        "Code": 0,
        "Audio": 0,
        "Video": 0,
        "Archives": 0,
        "Executables": 0,
        "Other": 0,
        "No Extension": 0
    }

    for file in files:
        extension = file.suffix.lower()
        
        if extension in images:
            category_counts["Images"] += 1
        elif extension in documents:
            category_counts["Documents"] += 1
        elif extension in code:
            category_counts["Code"] += 1
        elif extension in audio:
            category_counts["Audio"] += 1
        elif extension in video:
            category_counts["Video"] += 1
        elif extension in archives:
            category_counts["Archives"] += 1
        elif extension in executables:
            category_counts["Executables"] += 1
        elif not extension:
            category_counts["No Extension"] += 1
        else:
            category_counts["Other"] += 1
        
    return category_counts

