# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Git仓库管理模块
"""
import os.path

import git
from git.repo.fun import is_git_dir
from typing import List, Union


class GitManager:
    """
    Git仓库管理模块
    """

    def __init__(self, local_path: str, repo_path: str, branch: str = "main"):
        self.local_path = local_path
        self.repo_path = repo_path
        self.branch = branch
        self.repo: Union[git.Repo, None] = None
        self.initial()

    def initial(self):
        """初始化git仓库

        Returns:

        """
        if not os.path.exists(self.local_path):
            os.mkdir(self.local_path)

        git_local_path: str = os.path.join(self.local_path, ".git")
        if not is_git_dir(git_local_path):
            self.repo = git.Repo.clone_from(self.repo_path, to_path=self.local_path)
        else:
            self.repo = git.Repo(self.local_path)

    def commit(self, message: str):
        """提交更改信息到仓库

        Args:
            message: 信息内容

        Returns:

        """
        self.repo.git.add(".")
        self.repo.git.commit("-m", message)
        origin = self.repo.remote(name="origin")
        origin.push(refspec=f"{self.branch}:{self.branch}")
