import os
import pathlib

# I think this is the best implementation as it makes it easy to test without adding complexity
def yield_entries_to_remove(src, dest):
    """yields files and directories present in the destination that no longer exist in source"""
    # traverse topdown as removing a dir that is not empty would raise an error
    for path, dirs, files in os.walk(dest, topdown=False):
        relative_path = pathlib.Path(path).relative_to(dest)

        for file in files:
            dest_file = pathlib.Path(path) / file
            src_file = src / relative_path / file

            if not src_file.exists():
                yield dest_file

        for dir in dirs:
            dest_dir = pathlib.Path(path) / dir
            src_dir = src / relative_path / dir

            if not src_dir.exists():
                yield dest_dir


def remove_extra_entries(src, dest):
    for item in yield_entries_to_remove(src, dest):
        if item.is_file():
            item.unlink()
            print("Deleted file " + item.name)
        elif item.is_dir():
            item.rmdir()
            print("Deleted directory " + item.name)



"""
# this function is questionable as we could delete the files and dirs as we find them, instead of returning a list that we need to iterate again,
# but this way it is more testable and does not affect complexity
def get_entries_to_remove(src, dest):
    # returns a list of files and directories present in the destination that no longer exist in source
    files_to_remove = []
    dirs_to_remove = []
    for path, dirs, files in os.walk(dest):
        relative_path = pathlib.Path(path).relative_to(dest)

        for file in files:
            dest_file = pathlib.Path(path) / file
            src_file = src / relative_path / file

            if not src_file.exists():
                files_to_remove.append(dest_file)

        for dir in dirs:
            dest_dir = pathlib.Path(path) / dir
            src_dir = src / relative_path / dir
            if not src_dir.exists():
                dirs_to_remove.append(dest_dir)

    return files_to_remove, dirs_to_remove
"""