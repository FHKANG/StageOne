# !/usr/bin/python3
# -*- coding: utf-8 -*-
import fire
import os

from stage_one.config import sog
from stage_one.utils import file_handle
from stage_one.core.initializer import PysoInitializer


def init():
    """根据配置文件初始化工程目录

    Returns:

    """
    for project_name in sog.config:
        root_path = os.getcwd() + f"./{project_name}"
        # 初始化项目目录
        file_handle.mk_dir(root_path)
        # TODO:
        # 1. 初始化git
        # 2. 初始化配置文件
        # 3. 初始化版本管理
        initializer = PysoInitializer()
        initializer.init_project(root_path, sog.config.get(project_name))


def entry_point():
    fire.Fire({
        "init": init
    })

