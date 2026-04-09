import os
import shutil
import argparse
import logging
from config import FILE_TYPES, DEFAULT_FOLDER
from utils import get_logger

logger = get_logger()


def main():
    organize_files()


def get_unique_path(path):
    root, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = f"{root}_{counter}{extension}"
        counter += 1
    return path


def organize_files():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        help="folder path to organize",
        type=str,
    )
    parser.add_argument(
        "--dry_run",
        action="store_true",
        help="Simulate file organization without moving files",
    )
    args = parser.parse_args()

    SOURCE_DIR = args.path or os.path.expanduser("~/Downloads")

    total_files = 0
    moved_files = 0

    if os.path.basename(SOURCE_DIR) in FILE_TYPES:
        logger.info(f"Already inside categorized folder. Exiting.")
        return

    for file_name in os.listdir(SOURCE_DIR):
        if file_name.startswith("."):
            continue
        file_path = os.path.join(SOURCE_DIR, file_name)
        file_type_found = False
        if os.path.isfile(file_path):
            for folder, extensions in FILE_TYPES.items():
                if file_name.lower().endswith(tuple(extensions)):
                    file_type_found = True
                    target_folder = os.path.join(SOURCE_DIR, folder)
                    break
            if not file_type_found:
                target_folder = os.path.join(SOURCE_DIR, DEFAULT_FOLDER)

            os.makedirs(target_folder, exist_ok=True)

            destination = os.path.join(target_folder, file_name)
            destination = get_unique_path(destination)
            if args.dry_run:
                logger.info(f"[DRY RUN] Would move: {file_name} → {target_folder}")
            else:
                try:
                    shutil.move(file_path, destination)
                except Exception as e:
                    logger.error(f"Error moving {file_name}: {e}")
                else:
                    logger.info(f"Moved: {file_name} -> {target_folder}")
                    moved_files += 1
            total_files += 1
    logger.info(f"Processed: {total_files}, Moved: {moved_files}")


if __name__ == "__main__":
    main()
