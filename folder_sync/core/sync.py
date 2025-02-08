from folder_sync.utils.hash_file import compute_file_hash


def files_match(origin_path, dest_path):
    """compares the computed hash of two files, to verify if they are identical"""
    return compute_file_hash(origin_path) == compute_file_hash(dest_path)

