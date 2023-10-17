# !/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import os
from setuptools import find_packages, setup

this_directory = os.path.abspath(os.path.dirname(__file__))

if os.getcwd() != this_directory:
    print("You must run setup.py from the project root")
    exit(-1)


def find_version(*filepath):
    # Extract version information from filepath
    with open(os.path.join(".", *filepath)) as fp:
        version_match = re.search(
            r"^__version__ = ['\"]([^'\"]*)['\"]", fp.read(), re.M
        )
        if version_match:
            return version_match.group(1)
        print("Unable to find version string.")
        exit(-1)


setup(
    name="stage_one",
    version=find_version("stage_one", "version.py"),
    packages=find_packages(
        exclude=(
            "configs",
            "configs.*"
        )
    ),
    extras_require={"dev": ["pylint"]},
    entry_points={
        "console_scripts": [
            "pyso = stage_one.cli:entry_point",
        ],
    },
    # data_files=[("config", ["config/tree.yaml"])],
    package_data={"": ["*.yaml"]}
)
