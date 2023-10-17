# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from contextlib import contextmanager

import yaml
import json
from omegaconf import OmegaConf


class StageOneConfig:
    __DEFAULT_CONFIG_PATH = os.path.normpath(
        os.path.join(__file__, "../tree.yaml")
    )

    def __init__(self, config_file=None):
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

    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            keys = name.split(".")
            result = getattr(self.config, keys[0])
            for key in keys[1:]:
                result = getattr(result, key)
            return result

    def __getitem__(self, name):
        return self.__getattribute__(name)

    def __setattr__(self, name, value):
        if name == "config":
            object.__setattr__(self, name, value)
        try:
            # Can only set attribute if already exists
            object.__getattribute__(self, name)
            object.__setattr__(self, name, value)
        except AttributeError:
            dotlist = [f"{name}={value}"]
            update = OmegaConf.from_dotlist(dotlist)
            self.config = OmegaConf.merge(self.config, update)

    def __setitem__(self, name, value):
        self.__setattr__(name, value)

    @contextmanager
    def temp_override(self, override_dict):
        old_config = self.config
        try:
            dotlist = [f"{k}={v}" for k, v in override_dict.items()]
            update = OmegaConf.from_dotlist(dotlist)
            self.config = OmegaConf.merge(self.config, update)
            yield
        finally:
            self.config = old_config


class Tree:
    __DEFAULT_CONFIG_PATH = os.path.normpath(
        os.path.join(__file__, "../../../config/tree.yaml")
    )
