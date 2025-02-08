import hashlib


# based on https://www.geeksforgeeks.org/python-program-to-find-hash-of-file/
def compute_file_hash(file_path):
    """compute the md5 hash of a file"""
    md5 = hashlib.md5()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            md5.update(chunk)

    return md5.hexdigest()
