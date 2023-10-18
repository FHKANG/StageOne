# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
配置文件解析
"""
import os
import yaml


class StageOneConfig:
    """
    配置文件解析
    """
    __DEFAULT_CONFIG_PATH = os.path.normpath(
        os.path.join(__file__, "../tree.yaml")
    )

    def __init__(self, config_file=None):
        self.config = None
        self.load_config(config_file)

    def load_config(self, config_file):
        """Loads config from a yaml file"""
        if config_file is None:
            config_file = StageOneConfig.__DEFAULT_CONFIG_PATH

        # Use yaml to open stream for safe load
        with open(config_file) as stream:
            config_dict = yaml.safe_load(stream)
        # self.config = OmegaConf.create(config_dict)
        self.config = config_dict

    def set_config(self, config):
        if isinstance(config, StageOneConfig):
            self.config = config.config
        else:
            self.config = config
