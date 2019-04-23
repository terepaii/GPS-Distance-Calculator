#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Module to handle data loading and writing
"""

import jsonlines
import logging
import urllib.request as request

from urllib.error import HTTPError

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
_logger = logging.getLogger(__name__)


class DataHandler():

    def get_remote_data(self, url):
        """
        High level function to encapsulate downloading data and
        loading into memory
        """
        response = self._download_remote_dataset(url)
        return [obj for obj in self._load_jsonlines(response)]

    def write_data_to_file(self, dataset, output_file):
        """
        Write a list of dictionaries to an output file

        Args:
             dataset (list): A list of dictionaries
             output_file (string): A string indicating where to write output to
        """
        with jsonlines.open(output_file, mode='w') as writer:
            for obj in dataset:
                writer.write(obj)

    def _download_remote_dataset(self, url):
        """
        Function to retrieve a remote dataset

        Args:
            url (string): location of the dataset

        Returns:
            HTTPResponse: HTTP response containing jsonlines data in the case of a success

        Raises:
            HTTPError: In any case the request fails
        """
        try:
            response = request.urlopen(url)
        except HTTPError as e:
            _logger.error(f"Dataset retrieval failed with HTTP error: {e.code}")
            raise
        else:
            return response

    def _load_jsonlines(self, dataset):
        """
        Function to encapsulate a dataset into a jsonlines Reader object.

        Args:
            dataset (HTTPResponse): HTTPResponse encapsulating a dataset
        Returns:
            jsonlines.Reader: JSON Lines Reader object wrapping a HTTPResponse object
                              containing the full dataset

        Raises:
            TypeError: Invalid data was supplied to the function
        """
        try:
            reader = jsonlines.Reader(dataset)
        except TypeError:
            _logger.error("Invalid data supplied to function")
            raise
        return reader



