import pytest
from folder_sync.utils.hash_file import compute_file_hash

#TEST_DIR = "../testcases/hash/" originally used a testcases folder but found this https://docs.pytest.org/en/stable/how-to/tmp_path.html

def test_compute_file_hash(tmp_path):
    test_file = tmp_path / "test_hash.txt"
    test_file.write_text("Hello!!!")

    got = compute_file_hash(test_file)
    want = "0f5c512c77798eeb751bf68ba2d1de815d10dd921da46c77968c5c16fa645a6f"

    assert got == want

def test_compute_file_hash_empty(tmp_path):
    empty_file = tmp_path / "test_hash_empty.txt"
    empty_file.write_text("")

    got = compute_file_hash(empty_file)
    want = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

    assert got == want

def test_compute_file_hash_non_existent_file(tmp_path):
    non_existent_file = tmp_path / "this_file_does_not_exist.txt"

    with pytest.raises(FileNotFoundError):
        compute_file_hash(non_existent_file)

def test_compute_file_hash_directory(tmp_path):
    test_dir = tmp_path / "dir"
    test_dir.mkdir()

    with pytest.raises(PermissionError):
        compute_file_hash(test_dir)