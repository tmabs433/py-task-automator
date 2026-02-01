py-task-automator

A lightweight Python toolkit for automating common backend and operational tasks such as file processing, data transformation, API interactions, and scheduled workflows.

py-task-automator is designed to be simple, extensible, and easy to integrate into existing Python projects where repetitive tasks need to be handled reliably.

Why this project exists

Many backend and operational workflows involve repetitive tasks that are often re-implemented across projects — file handling, batch processing, API calls, logging, and basic validations.

This project provides a clean and reusable foundation for those tasks, allowing developers to focus on business logic instead of boilerplate automation code.

Features

File and directory operations (create, move, archive, clean up)

CSV and structured data processing

HTTP API requests with retries and error handling

Task logging and basic monitoring

Simple task orchestration helpers

Extensible design for custom automation needs

Installation

Clone the repository and install dependencies:

git clone https://github.com/tmabs433/py-task-automator.git
cd py-task-automator
pip install -r requirements.txt


Python 3.10+ is recommended.

Basic usage

A simple example of running an automated task:

from automator.tasks import FileCleaner

cleaner = FileCleaner(
    target_directory="logs/",
    max_age_days=7
)

cleaner.run()


This will remove files older than the specified number of days and log the outcome.

More examples can be found in the examples/ directory.

Project structure
py-task-automator/
 ├── automator/
 │   ├── tasks/
 │   ├── utils/
 │   └── logging/
 ├── tests/
 ├── examples/
 ├── README.md
 └── requirements.txt


The project is structured to keep automation logic modular and easy to extend.

Design principles

Clarity over cleverness – readable code is preferred over complex abstractions

Practical automation – focused on real operational use cases

Minimal dependencies – only what is necessary

Extensibility – easy to add new task types

Use cases

Automating routine backend maintenance

Batch processing of files or datasets

Scheduled data cleanup jobs

Simple workflow orchestration for internal tools

Supporting DevOps and data operations tasks

Testing

Tests are written using pytest.

To run tests:

pytest

Contributing

Contributions are welcome.

If you would like to contribute:

Fork the repository

Create a feature branch

Add tests where applicable

Submit a pull request with a clear description

Please keep changes focused and well documented.

Roadmap

Planned improvements include:

Config-driven task definitions

CLI support for common automation tasks

Improved logging and metrics

Additional built-in task types

License

This project is licensed under the MIT License.

Author

Babatunde Mabinuori
Senior Software Engineer (Python)