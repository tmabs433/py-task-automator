import argparse

from automator.tasks.file_cleaner import FileCleaner
from automator.tasks.csv_cleaner import CSVCleaner


def main():
    parser = argparse.ArgumentParser(
        description="py-task-automator command line interface"
    )

    subparsers = parser.add_subparsers(dest="command")

    # ---- clean-files command ----
    clean_files = subparsers.add_parser(
        "clean-files",
        help="Remove files older than a specified number of days"
    )
    clean_files.add_argument(
        "--path",
        required=True,
        help="Target directory to clean"
    )
    clean_files.add_argument(
        "--days",
        type=int,
        default=7,
        help="Maximum file age in days (default: 7)"
    )


    clean_csv = subparsers.add_parser(
        "clean-csv",
        help="Clean a CSV file by removing empty rows"
    )
    clean_csv.add_argument(
        "--input",
        required=True,
        help="Path to input CSV file"
    )
    clean_csv.add_argument(
        "--output",
        required=True,
        help="Path to output cleaned CSV file"
    )


    args = parser.parse_args()

    if args.command == "clean-files":
        cleaner = FileCleaner(
            target_directory=args.path,
            max_age_days=args.days
        )
        removed = cleaner.run()
        print(f"{removed} files removed.")

    elif args.command == "clean-csv":
        cleaner = CSVCleaner(
            input_file=args.input,
            output_file=args.output
        )
        rows = cleaner.run()
        print(f"{rows} rows written.")

    else:
        parser.print_help()






if __name__ == "__main__":
    main()
