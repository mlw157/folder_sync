import os
import pathlib
import shutil

from folder_sync.core.cleanup import remove_extra_entries
from folder_sync.utils.hash_file import compute_file_hash

# no need to test this
def files_match(origin_path, dest_path):
    """compares the computed hash of two files, to verify if they are identical"""
    return compute_file_hash(origin_path) == compute_file_hash(dest_path)

def synchronize_dirs(src, dest):
    """synchronize two directories"""
    # remove files and directories that are no longer present in src
    remove_extra_entries(src, dest)

    for path, dirs, files in os.walk(src):
        relative_path = pathlib.Path(path).relative_to(src)
        dest_path = dest / relative_path

        if not dest_path.exists():
            dest_path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {dest_path}")

        for file in files:
            dest_file = dest_path / file
            src_file = pathlib.Path(path) / file

            # if the file does not exist in dest folder or the content has been changed
            if not dest_file.exists() or not files_match(src_file, dest_file):
                shutil.copy2(src_file, dest_file)
                print(f"Copied/updated file: {src_file} -> {dest_file}")


    return None