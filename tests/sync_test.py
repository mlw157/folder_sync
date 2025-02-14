from venv import logger

import pytest
from folder_sync.core.sync import synchronize_dirs

class TestSyncDirectories:
    def test_synchronize_dirs(self, tmp_path):
        src = tmp_path / "src"
        src.mkdir()
        dest = tmp_path / "dest"
        dest.mkdir()

        dest_only_file = dest / "dest_only_file.txt"
        dest_only_file.write_text("this file is only in dest")
        dest_only_dir = dest / "dest_only_dir"
        dest_only_dir.mkdir()

        src_only_dir = src / "src_only_dir"
        src_only_dir.mkdir()
        src_only_file = src_only_dir / "src_only_file.txt"
        src_only_file.write_text("this file is only in src")

        mutual_file_src = src / "mutual_file.txt"
        mutual_file_src.write_text("this file is in src and dest")
        mutual_file_dest = dest / "mutual_file.txt"
        mutual_file_dest.write_text("this file is in src and dest")

        mutual_dir_src = src / "mutual_dir"
        mutual_dir_src.mkdir()
        mutual_dir_dest = dest / "mutual_dir"
        mutual_dir_dest.mkdir()

        changed_file_src = src / "changed_file.txt"
        changed_file_src.write_text("changed content")
        changed_file_dest = dest / "changed_file.txt"
        changed_file_dest.write_text("original content")

        synchronize_dirs(src, dest, logger)

        assert not dest_only_dir.exists()
        assert not dest_only_file.exists()

        assert (dest / "src_only_dir").exists()
        assert (dest / "src_only_dir" / "src_only_file.txt").exists()

        assert mutual_file_dest.exists()
        assert mutual_dir_dest.exists()

        assert changed_file_dest.exists()
        assert changed_file_dest.read_text() == "changed content"

    def test_synchronize_dirs_updated_files(self, tmp_path):
        src = tmp_path / "src"
        src.mkdir()
        dest = tmp_path / "dest"
        dest.mkdir()

        updated_file_src = src / "changed_file.txt"
        updated_file_src.write_text("changed content")
        updated_file_dest = dest / "changed_file.txt"
        updated_file_dest.write_text("original content")

        synchronize_dirs(src, dest, logger)

        assert updated_file_dest.exists()
        assert updated_file_dest.read_text() == "changed content"

    def test_synchronize_dirs_nested_directories(self, tmp_path):
        src = tmp_path / "src"
        src.mkdir()
        dest = tmp_path / "dest"
        dest.mkdir()

        nested_dir = src / "dir1" / "dir2"
        nested_dir.mkdir(parents=True)
        nested_file = nested_dir / "nested_file.txt"
        nested_file.write_text("nested file")

        synchronize_dirs(src, dest, logger)

        assert (dest / "dir1" / "dir2" / "nested_file.txt").exists()

    def test_synchronize_dirs_src_does_not_exist(self, tmp_path):
        src = tmp_path / "src"

        dest = tmp_path / "dest"
        dest.mkdir()

        synchronize_dirs(src, dest, logger) # no asserts but to test it runs without an error

    def test_synchronize_dirs_dest_does_not_exist(self, tmp_path):
        src = tmp_path / "src"
        src.mkdir()

        dest = tmp_path / "dest"

        synchronize_dirs(src, dest, logger)

        assert dest.exists() # dest will be created

