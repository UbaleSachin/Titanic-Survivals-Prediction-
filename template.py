import os
from pathlib import Path

project_name = "titanic_survival_predictions"

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/pipeline/__init__.py",
    "notebook/data",
    "templates/",
    "main.py",
    "requirements.txt",
    "setup.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath, "w") as f:
            pass

    else:
        print(f"{filename} already exists")