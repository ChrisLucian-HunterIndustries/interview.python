import re
from pathlib import Path

from setuptools import setup, find_packages

HERE = Path(__file__).parent
_version_file_contents = (HERE / "project" / "version.py").read_text()
VERSION = re.search(r'"(.*)"', _version_file_contents).group(1)

setup(
    name="interview",
    version=VERSION,
   python_requires=">=3.6.1",
    packages=find_packages(exclude=["tests*"]),
)
