import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"
list_of_files =[".github/worlflows/.gitkeep",
f"src/{project_name}/__init__.py",
f"src/{project_name}/components/__init__.py",
f"src/{project_name}/utils/common.py",
f"src/{project_name}/logging/__init__.py",
f"src/{project_name}/config/__init__.py",
f"src/{project_name}/config/configuration.py",
f"src/{project_name}/config/configuration.py",
f"src/{project_name}/pipeline/__init__.py",
f"src/{project_name}/entity/__init__.py",
f"src/{project_name}/constants/__init__.py",
"config/config.yaml",
"params.yaml",
"app.py",
"main.py",
"Dockerfile",
"requirenments.txt",
"setup.py",
"research/trails.ipynb"


]
for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)

    if(filedir != ""):
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating file directory with name:{filedir} for the file {filename}")
    if(not os.path.exists(filename) or (os.path.getsize(file_path)==0)):
        with open(file_path,'w') as f:
            pass
            logging.info(f"creating empty {file_path}")
    else:
        logging.info(f"{filename} is already exist")
        