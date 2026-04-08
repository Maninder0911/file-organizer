import os
import shutil
import argparse
from config import FILE_TYPES


def main():
    organize_files()

def get_unique_path(path):
    root, extension = os.path.splitext(path)
    counter = 1

    while(os.path.exists(path)):
        path = f"{root}_{counter}{extension}"
        counter+=1
    return path


def organize_files():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        help="folder path to organize",
        type=str,
    )
    args = parser.parse_args()

    SOURCE_DIR = args.path or os.path.expanduser("~/Downloads")

    if os.path.basename(SOURCE_DIR) in FILE_TYPES:
        print("[INFO] Already inside categorized folder. Exiting.")
        return

    for file_name in os.listdir(SOURCE_DIR):
        file_path = os.path.join(SOURCE_DIR, file_name)
        file_type_found = False
        if os.path.isfile(file_path):
            for folder,extensions in FILE_TYPES.items():
                if file_name.lower().endswith(tuple(extensions)):
                    file_type_found = True
                    target_folder = os.path.join(SOURCE_DIR, folder)                   
                    break
            if not file_type_found:
                target_folder = os.path.join(SOURCE_DIR, "Others")
                
            os.makedirs(target_folder, exist_ok=True)
                    
            destination = os.path.join(target_folder, file_name)
            destination = get_unique_path(destination)

            try:
                shutil.move(file_path, destination)
            except Exception as e:
                print(f"Error moving {file_name}: {e}")
            else:
                print(f"[INFO] Moved: {file_name} → {target_folder}")       
                    

if __name__ == "__main__":
    main()
