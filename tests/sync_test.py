from folder_sync.core.sync import yield_entries_to_remove, remove_extra_entries


class TestYieldEntriesToRemove:
    """tests for the yield_entries_to_remove function"""
    def test_yield_entries_to_remove(self, tmp_path):
        src = tmp_path / "src"
        src.mkdir()
        dest = tmp_path / "dest"
        dest.mkdir()

        dest_only_file = dest / "dest_only_file.txt"
        dest_only_file.write_text("this file is only in dest")
        dest_only_dir = dest / "dest_only_dir"
        dest_only_dir.mkdir()

        mutual_file_src = src / "mutual_file.txt"
        mutual_file_src.write_text("this file is in src and dest")
        mutual_file_dest = dest / "mutual_file.txt"
        mutual_file_dest.write_text("this file is in src and dest")

        mutual_dir_src = src / "mutual_dir"
        mutual_dir_src.mkdir()
        mutual_dir_dest = dest / "mutual_dir"
        mutual_dir_dest.mkdir()

        got = set(yield_entries_to_remove(src, dest))
        want = {dest_only_file, dest_only_dir}

        assert got == want

    def test_yield_entries_to_remove_empty(self, tmp_path):
        src = tmp_path / "src"
        src.mkdir()
        dest = tmp_path / "dest"
        dest.mkdir()

        got = len(set(yield_entries_to_remove(src, dest)))
        want = 0

        assert got == want

    def test_yield_entries_to_remove_same_file_different_dirs(self, tmp_path):
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

        got = set(yield_entries_to_remove(src, dest))
        want = {dest_file, dir2}

        assert got == want

    def test_yield_entries_to_remove_no_match(self, tmp_path):
        src = tmp_path / "src"
        src.mkdir()
        dest = tmp_path / "dest"
        dest.mkdir()

        mutual_file_src = src / "mutual_file.txt"
        mutual_file_src.write_text("this file is in src and dest")
        mutual_file_dest = dest / "mutual_file.txt"
        mutual_file_dest.write_text("this file is in src and dest")

        got = len(set(yield_entries_to_remove(src, dest)))
        want = 0

        assert got == want


class TestRemoveExtraEntries:
    def test_remove_extra_entries(self, tmp_path):
        src = tmp_path / "src"
        src.mkdir()
        dest = tmp_path / "dest"
        dest.mkdir()

        dest_only_file = dest / "dest_only_file.txt"
        dest_only_file.write_text("this file is only in dest")
        dest_only_dir = dest / "dest_only_dir"
        dest_only_dir.mkdir()

        mutual_file_src = src / "mutual_file.txt"
        mutual_file_src.write_text("this file is in src and dest")
        mutual_file_dest = dest / "mutual_file.txt"
        mutual_file_dest.write_text("this file is in src and dest")

        mutual_dir_src = src / "mutual_dir"
        mutual_dir_src.mkdir()
        mutual_dir_dest = dest / "mutual_dir"
        mutual_dir_dest.mkdir()

        remove_extra_entries(src, dest)

        assert not dest_only_file.exists()
        assert not dest_only_dir.exists()
        assert mutual_dir_dest.exists()
        assert mutual_file_dest.exists()


    def test_remove_extra_entries_empty(self, tmp_path):
        src = tmp_path / "src"
        src.mkdir()
        dest = tmp_path / "dest"
        dest.mkdir()

        remove_extra_entries(src, dest) # no asserts but to test it runs without an error

