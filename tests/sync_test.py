from folder_sync.core.sync import sync_folders, get_files_to_remove

def test_sync(tmp_path):
    test_file1 = tmp_path / "test_file1.txt"
    test_file2 = tmp_path / "test_file2.txt"
    test_dir = tmp_path / "dir"
    test_dir.mkdir()

    test_file3 = test_dir / "test_file3.txt"


    test_file1.write_text("hello1")
    test_file2.write_text("hello2")
    test_file3.write_text("hello3")

    sync_folders(tmp_path, None)


class TestGetFilesToRemove:
    """tests for the get_files_to_remove function"""

    def test_get_files_to_remove(self, tmp_path):
        src = tmp_path / "src"
        src.mkdir()
        dest = tmp_path / "dest"
        dest.mkdir()

        extra_dir = dest / "dir"
        extra_dir.mkdir()

        mutual_file_src = src / "mutual_file.txt"
        mutual_file_src.write_text("this file is in src and dest")
        mutual_file_dest = dest / "mutual_file.txt"
        mutual_file_dest.write_text("this file is in src and dest")

        dest_only_file1 = dest / "dest_only_file1.txt"
        dest_only_file1.write_text("this file is only in dest folder")
        dest_only_file2 = dest / "dest_only_file2.txt"
        dest_only_file2.write_text("this file is only in dest folder")
        dest_only_file3 = extra_dir / "dest_only_file3.txt"
        dest_only_file3.write_text("this file is only in dest folder")

        got = set(get_files_to_remove(src, dest))
        want = {dest_only_file1, dest_only_file2, dest_only_file3}

        assert got == want

    def test_get_files_to_remove_empty(self, tmp_path):
        src = tmp_path / "src"
        src.mkdir()
        dest = tmp_path / "dest"
        dest.mkdir()

        got = len(get_files_to_remove(src, dest))
        want = 0

        assert got == want

    def test_get_files_to_remove_same_file_different_dirs(self, tmp_path):
        src = tmp_path / "src"
        src.mkdir()
        dest = tmp_path / "dest"
        dest.mkdir()

        dir1 = src / "src_dir"
        dir1.mkdir()
        dir2 = dest / "dest_dir"
        dir2.mkdir()

        src_file = dir1 / "same_name.txt"
        src_file.write_text("same content")
        dest_file = dir2 / "same_name.txt"
        dest_file.write_text("same content")

        got = set(get_files_to_remove(src, dest))
        want = {dest_file}

        assert got == want

    def test_get_files_to_remove_no_match(self, tmp_path):
        src = tmp_path / "src"
        src.mkdir()
        dest = tmp_path / "dest"
        dest.mkdir()

        mutual_file_src = src / "mutual_file.txt"
        mutual_file_src.write_text("this file is in src and dest")
        mutual_file_dest = dest / "mutual_file.txt"
        mutual_file_dest.write_text("this file is in src and dest")

        got = len(get_files_to_remove(src, dest))
        want = 0

        assert got == want