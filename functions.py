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
        category = categorize_file(file)
        category_counts[category] += 1

        
    return category_counts

def display_extension_summary(category_counts):
    """Displays the number of files in each category."""
    for category, count in category_counts.items():
        print(f"{category}: {count}")
    
def categorize_file(file):
    """Returns the category of a file based on its extension."""

    extension = file.suffix.lower()

    if extension in images:
        return "Images"
    elif extension in documents:
        return "Documents"
    elif extension in code:
        return "Code"
    elif extension in audio:
        return "Audio"
    elif extension in video:
        return "Video"
    elif extension in archives:
        return "Archives"
    elif extension in executables:
        return "Executables"
    elif not extension:
        return "No Extension"
    else:
        return "Other"

def create_category_folders(folder_path, files):
    """Creates category folders for files if they do not already exist."""
    for file in files:
        category = categorize_file(file)
        category_folder = folder_path / category

        if not category_folder.exists():
            category_folder.mkdir()

def preview_moves(files, folder_path):
    """Previews each file's destination and asks the user to confirm the file moves."""
    if not files:
        print("\nFolder is empty!\n")
        return False
    for file in files:
        category = categorize_file(file)
        print(f"{file.name} --> {category}")
    
    choice = input("Would you like to confirm these changes? (Y/N)").strip().upper()
    if choice == 'Y':
        return True
    elif choice == 'N':
        return False
    else:
        print("\nInvalid choice.\n")
        return False

def move_files(files, folder_path, confirmed):
    """Moves confirmed files into their category folders while skipping duplicates."""
    if not confirmed:
        return
    
    moved_count = 0
    skipped_count = 0

    for file in files:
        category = categorize_file(file)
        category_folder = folder_path / category
        destination = category_folder / file.name
    
        if not destination.exists():
            file.rename(destination)
            moved_count += 1
        else:
            skipped_count += 1
    
    print(f"\n[{moved_count}] Files Moved Successfully!")
    print(f"[{skipped_count}] Files Skipped.\n")