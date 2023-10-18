# !/usr/bin/python3
# -*- coding: utf-8 -*-
from stage_one.utils import file_handle


class PysoInitializer:

    def __init__(self):
        pass

    def initial(self, root_path: str, tree: dict):
        """初始化项目目录

        Args:
            root_path: 目录根路径
            tree: 文档树

        Returns:

        """

        for info in tree.keys():

            if tree.get(info) is None:
                file_handle.mk_dir(f"{root_path}/{info}")
            elif isinstance(tree.get(info), dict):
                file_handle.mk_dir(f"{root_path}/{info}")
                self.initial(f"{root_path}/{info}", tree=tree.get(info))
            else:
                self.mk_file(path=f"{root_path}/{tree.get(info)}")

    @staticmethod
    def mk_file(path: str):
        """根据不同的文件格式创建文件

        Args:
            path: 文件路径

        Returns:

        """
        if ".py" in path:
            file_handle.mk_py(file_path=path)
        elif "CHANGELOG.md" in path:
            file_handle.mk_changelog(file_path=path)
        else:
            file_handle.mk_file(file_path=path, file_text="")
