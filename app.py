import argparse

from folder_sync.core.sync import synchronize_dirs


def main():
    print("Running synchronizer")
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Source folder path")
    parser.add_argument("replica", help="Replica folder path")

    args = parser.parse_args()

    try:
        synchronize_dirs(args.source, args.replica)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()