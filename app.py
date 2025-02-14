import argparse
import time
from venv import logger

from folder_sync.core.sync import synchronize_dirs
from folder_sync.utils.logger import init_logger


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Source folder path")
    parser.add_argument("dest", help="Replica folder path")
    parser.add_argument("interval", type=int, help="Synchronization interval (seconds)")
    parser.add_argument("log_file", help="Log file path")

    args = parser.parse_args()
    logger = init_logger(args.log_file)


    # here we use prints instead of the logger because we don't have to save these messages in the log file, only creation/copying/removal operations
    print("Starting synchronization...")
    while True:
        try:
            print("Synchronizing...")
            synchronize_dirs(args.source, args.dest, logger)
        except Exception as e:
            print(f"Error synchronizing: {e}")
        finally:
            time.sleep(args.interval)

if __name__ == "__main__":
    main()