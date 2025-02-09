import hashlib


# based on https://www.geeksforgeeks.org/python-program-to-find-hash-of-file/
# we are using sha256 as md5 is vulnerable to hash collision
def compute_file_hash(file_path):
    """compute the sha256 hash of a file"""
    md5 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            md5.update(chunk)

    return md5.hexdigest()
