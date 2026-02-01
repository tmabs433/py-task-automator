from pathlib import Path
from datetime import datetime, timedelta

from automator.utils.logger import get_logger


class FileCleaner:
    """
    Cleans files older than a specified number of days
    from a target directory.
    """

    def __init__(self, target_directory: str, max_age_days: int = 7):
        self.target_directory = Path(target_directory)
        self.max_age_days = max_age_days
        self.logger = get_logger(self.__class__.__name__)

    def run(self) -> int:
        """
        Execute the cleanup process.

        Returns:
            int: Number of files removed
        """
        if not self.target_directory.exists():
            self.logger.warning(
                f"Directory does not exist: {self.target_directory}"
            )
            return 0

        cutoff_date = datetime.now() - timedelta(days=self.max_age_days)
        removed_files = 0

        for file_path in self.target_directory.iterdir():
            if file_path.is_file():
                last_modified = datetime.fromtimestamp(
                    file_path.stat().st_mtime
                )
                if last_modified < cutoff_date:
                    file_path.unlink()
                    removed_files += 1
                    self.logger.info(f"Removed file: {file_path.name}")

        self.logger.info(
            f"Cleanup completed. {removed_files} files removed."
        )
        return removed_files
