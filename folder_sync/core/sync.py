import os
import pathlib
from folder_sync.utils.hash_file import compute_file_hash


def files_match(origin_path, dest_path):
    """compares the computed hash of two files, to verify if they are identical"""
    return compute_file_hash(origin_path) == compute_file_hash(dest_path)

def sync_folders(src, dest):
    #for path, dirs, files in os.walk(src):
    return None

# should it get folders too or different function?
def get_files_to_remove(src, dest):
    """returns a list of files present in the destination that no longer exist in source"""
    files_to_remove = []
    for path, dirs, files in os.walk(dest):
        relative_path = pathlib.Path(path).relative_to(dest)

        for file in files:
            dest_file = pathlib.Path(path) / file
            src_file = src / relative_path / file

            if not src_file.exists():
                files_to_remove.append(dest_file)

    return files_to_remove