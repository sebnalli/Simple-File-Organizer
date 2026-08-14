from pathlib import Path

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

    valid_items = []

    for item in folder_path.iterdir:
        if item.is_file():
            name = item.name
            extension = item.suffix

            valid_items.append(item)
        
    return valid_items

