# !/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import fire
import subprocess
from stage_one.config import sog
from stage_one.utils import file_handle
from stage_one.core.git_manager import GitManager
from stage_one.core.initializer import PysoInitializer


def init():
    """根据配置文件初始化工程目录
        强制要求工程配置GIT仓库来管理代码
    Returns:

    """
    # 初始化工程仓库
    repository_name = input("Please enter the repository name: ")
    remote_url = input("Please enter the repository url: ")
    # remote_url = "http://gitlab.info.dbappsecurity.com.cn/algorithm/interns/test.git"
    git_object = GitManager(local_path=repository_name, repo_path=remote_url)

    # 初始化项目目录
    root_path = os.getcwd() + f"./{repository_name}"
    initializer = PysoInitializer()
    initializer.initial(root_path, sog.config)

    # 初始化Commit
    print(">>>" * 10 + " inital commit ")
    git_object.commit("initial")


def entry_point():
    fire.Fire({
        "init": init
    })


if __name__ == "__main__":
    init()
