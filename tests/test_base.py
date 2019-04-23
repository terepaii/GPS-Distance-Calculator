#!/usr/bin/env python37
# -*- coding: utf-8 -*-

"""
Module used as the base TestClass
"""

import json

class BaseTestClass():
    @classmethod
    def setup_class(cls):
        with open('config/test_config.json') as json_config:
            cls.config = json.load(json_config)["TEST"]
