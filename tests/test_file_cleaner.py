import tempfile
from pathlib import Path

from automator.tasks.file_cleaner import FileCleaner


def test_file_cleaner_removes_old_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        old_file = temp_path / "old.txt"
        old_file.write_text("test")

        cleaner = FileCleaner(
            target_directory=temp_dir,
            max_age_days=0
        )
        removed = cleaner.run()

        assert removed == 1
