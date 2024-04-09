import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = "cnnClassifier"

files_list = [
    ".github/work/flows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for file_path in files_list:
    file = Path(file_path)
    filedir = file.parent

    # Create directories if they don't exist
    if filedir and not filedir.exists():
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    # Check if file needs to be created (does not exist or is empty)
    if not file.exists() or file.stat().st_size == 0:
        with open(file, "w") as f:
            pass
        logging.info(f"Creating empty file: {file}")
    else:
        logging.info(f"{file.name} already exists")
