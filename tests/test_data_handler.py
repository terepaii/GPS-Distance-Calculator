#!/usr/bin/env python37
# -*- coding: utf-8 -*-

"""
Test module for the DataHandler class
"""

import pytest

from .test_base import BaseTestClass
from gps_distance_calculator.data_handler import DataHandler

from urllib.error import HTTPError


class TestDataHandler(BaseTestClass):


    def setup(self):
        self.url = self.config["DATASET_URL"]
        self.data_handler = DataHandler()

    # Test downloading remote dataset
    def test_download_remote_dataset_success(self):
        response = self.data_handler._download_remote_dataset(self.url)

        assert response.code == 200
        assert response.url == self.url

    def test_download_remote_dataset_invalid_url_failure(self):
        url = "https://s3.amazonaws.com/intercom-take-home-test/customers.json"

        with pytest.raises(HTTPError):
            self.data_handler._download_remote_dataset(url)

    # Test load_jsonlines into memory
    def test_load_jsonlines_invalid_data(self):
        with pytest.raises(TypeError):
            self.data_handler._load_jsonlines(123)

    # Test retrieving data and loading into memory
    def test_get_data_success(self):
        result = self.data_handler.get_remote_data(self.url)
        for obj in result :
            assert 'latitude' in obj
            assert 'longitude' in obj
            assert 'user_id' in obj
            assert 'name' in obj

    def test_get_data_invalid_url_failure(self):
        url = "https://s3.amazonaws.com/intercom-take-home-test/customers.json"
        with pytest.raises(HTTPError):
            self.data_handler.get_remote_data(url)