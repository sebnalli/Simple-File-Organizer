from functions import (
    get_folder_path,
    validate_folder,
    scan_files,
    display_files,
    count_extensions,
    display_extension_summary,
    categorize_file,
    create_category_folders,
    preview_moves,
    move_files
)

def run_program():
    """Runs the file organizer workflow from folder selection through file organization."""
    while True:

        folder_path = get_folder_path()

        if not validate_folder(folder_path):
            continue

        files = scan_files(folder_path)

        display_files(files)

        category_counts = count_extensions(files)

        display_extension_summary(category_counts)

        confirmed = preview_moves(files, folder_path)
        if not confirmed:
            print("\nChanges cancelled.\n")
            continue

        create_category_folders(folder_path, files)

        move_files(files, folder_path, confirmed)

        break

run_program()