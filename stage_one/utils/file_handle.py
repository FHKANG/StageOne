# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os


def mk_dir(dir_path: str):
    """创建文件夹

    Args:
        dir_path: 文件夹路径

    Returns:

    """
    os.mkdir(dir_path)


def mk_file(file_path: str, file_text: str):
    """创建文件

    Args:
        file_path: 文件名

    Returns:

    """
    with open(file_path, mode="w", encoding="utf-8") as fp:
        fp.write(file_text)


def mk_py(file_path: str):
    """构建Python文件

    Args:
        file_path: 文件路径

    Returns:

    """
    file_text = "\n".join(
        [
            "# !/usr/bin/python3",
            "# -*- coding: utf-8 -*-",
            ""
        ]
    )
    mk_file(file_path=file_path, file_text=file_text)


def mk_changelog(file_path: str):
    file_text = "\n".join(
        [
            "# Changelog",
            "",
            "All notable changes to this project will be documented in this file.",
            "",
            "The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),",
            "and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).",
            "# Types of changes",
            "Added  for new features. Changed for changes in existing functionality. Deprecated for soon-to-be removed features. Removed for now removed features. Fixed for any bug fixes. Security in case of vulnerabilities.",
            ""
        ]
    )
    mk_file(file_path=file_path, file_text=file_text)
