#!/usr/bin/env python37
# -*- coding: utf-8 -*-

"""
Test module for the Calculator class
"""

from .test_base import BaseTestClass
from gps_distance_calculator.calculator import Calculator


class TestCalculator(BaseTestClass):

    def setup(self):
        self.calculator = Calculator()

    # Test Degrees To Radians
    def test_degrees_to_radians_success(self):
        assert self.calculator.degrees_to_radians(1) == 0.01745

    def test_degrees_to_radians_negative_success(self):
        assert self.calculator.degrees_to_radians(-1) == -0.01745

    def test_degrees_to_radians_over_360_success(self):
        assert self.calculator.degrees_to_radians(361) == 6.30064


    # Test Converting GPS Coordinates
    def test_convert_gps_coordinates_to_radians_success(self):
        test_coords = {"latitude": 1, "longitude": -1}
        result = self.calculator.convert_gps_coordinates_to_radians(test_coords)

        assert result == {"latitude": 0.01745, "longitude": -0.01745}


    # Test Calculating distance between 2 GPS points
    def test_calculate_distance_with_same_coordinates_success(self):
        origin_coords = {"latitude": 53.3391919, "longitude": -6.2578313}
        desination_coords = {"latitude": 53.3391919, "longitude": -6.2578313}

        result = self.calculator.calculate_distance(origin_coords, desination_coords)
        assert result == 0

    def test_calculate_distance_with_different_coordinates_success(self):
        origin_lat = self.config["ORIGIN_COORDINATES"]["LAT"]
        origin_lon = self.config["ORIGIN_COORDINATES"]["LON"]
        origin_coords = {"latitude": origin_lat, "longitude": origin_lon}
        desination_coords = {"latitude": 52.986375, "longitude": -6.043701}

        result = self.calculator.calculate_distance(origin_coords, desination_coords)
        assert result == 41.70465


    def test_is_in_range_returns_true_success(self):
        origin_lat = self.config["ORIGIN_COORDINATES"]["LAT"]
        origin_lon = self.config["ORIGIN_COORDINATES"]["LON"]
        origin_coords = {"latitude": origin_lat, "longitude": origin_lon}
        desination_coords = {"latitude": 52.986375, "longitude": -6.043701}

        result = self.calculator.is_in_range(100, origin_coords, desination_coords)

        assert result is True

    def test_is_in_range_returns_false_success(self):
        origin_lat = self.config["ORIGIN_COORDINATES"]["LAT"]
        origin_lon = self.config["ORIGIN_COORDINATES"]["LON"]
        origin_coords = {"latitude": origin_lat, "longitude": origin_lon}
        desination_coords = {"latitude": 100, "longitude": -6.043701}

        result = self.calculator.is_in_range(100, origin_coords, desination_coords)

        assert result is False

