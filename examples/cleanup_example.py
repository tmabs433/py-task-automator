from automator.tasks.file_cleaner import FileCleaner

if __name__ == "__main__":
    cleaner = FileCleaner(
        target_directory="logs",
        max_age_days=7
    )
    cleaner.run()
