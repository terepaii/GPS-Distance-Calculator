#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

"""
Main file to demonstrate GPS Distance Calculator
"""

import json

from gps_distance_calculator.calculator import Calculator
from gps_distance_calculator.data_handler import DataHandler


class Runner():

    def __init__(self):
        self.calculator = Calculator()
        self.data_handler = DataHandler()

        with open('config/config.json') as json_config:
            self.config = json.load(json_config)['DEFAULT']

    def run(self):

        """
        Main method
        """

        # Get remote dataset
        url = self.config['DATASET_URL']
        dataset = self.data_handler.get_remote_data(url)

        # Filter by range
        range = self.config['RANGE']
        origin = {'latitude': self.config['ORIGIN_COORDINATES']['LAT'],
                  'longitude': self.config['ORIGIN_COORDINATES']['LON']}
        objects_in_range = []
        for obj in dataset:
            destination = {'latitude': obj['latitude'],
                           'longitude': obj['longitude']}
            if self.calculator.is_in_range(range, origin, destination):
                objects_in_range.append(obj)

        # Sort objects by user ID
        sorted_objects_in_range = sorted(objects_in_range, key=lambda x: x['user_id'])

        # Output to file
        output_file = self.config['OUTPUT_FILE']
        self.data_handler.write_data_to_file(sorted_objects_in_range, output_file)

if __name__ == "__main__":
    runner = Runner()
    runner.run()