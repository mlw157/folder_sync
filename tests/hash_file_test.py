import pytest

from folder_sync.utils.hash_file import compute_file_hash

TEST_DIR = "../testcases/hash/"

def test_compute_file_hash():
    got = compute_file_hash(TEST_DIR + "test_hash.txt")
    want = "fdb6c763a7a4e9e6ce1545d454bafce9"

    assert got == want

def test_compute_file_hash_empty():
    got = compute_file_hash(TEST_DIR + "test_hash_empty.txt")
    want = "d41d8cd98f00b204e9800998ecf8427e"

    assert got == want

def test_compute_file_hash_non_existent_file():
    with pytest.raises(FileNotFoundError):
        compute_file_hash(TEST_DIR + "this_file_does_not_exist_txt")

def test_compute_file_hash_image():
    got = compute_file_hash(TEST_DIR + "test_hash_image.png")
    want = "0e55ab45b2b4e9c206cf6eb1dba873c4"

    assert got == want

def test_compute_file_hash_directory():
    with pytest.raises(PermissionError):
        compute_file_hash(TEST_DIR + "dir")