import setuptools
from typing import List

__version__ = "0.0.0"
REPO_NAME = "Text-Summarisation"
AUTHOR_NAME = "pankajventure7"
SRC_REPO ="textSummarizer"
AUTHOR_EMAIL = "pankajcse107@gmail.com"



setuptools.setup(
name=SRC_REPO,
version=__version__,
author=AUTHOR_NAME,
author_email=AUTHOR_EMAIL,
url = f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
package_dir={"":"src"},

packages=setuptools.find_packages(where="src")


)


