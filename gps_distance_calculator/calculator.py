#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Module to compute the the great-circle distance between two GPS
coordinates
"""

import logging

from math import asin, cos, pi, sin, sqrt


logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
_logger = logging.getLogger(__name__)


EARTH_RADIUS_IN_KM = 6371

class Calculator():

    def is_in_range(self, range, origin_in_degrees, destination_in_degrees):
        """
        Function to encapsulate figuring out if two GPS coordinates are within a
        given range

        Args:
            range: The maximum range between two GPS coordinates
            origin_in_degrees: Origin GPS coordinates
            destination_in_degrees: Destination GPS coordinates

        Returns:
            bool: Whether the GPS coordinates are in a given range
        """
        return self.calculate_distance(origin_in_degrees, destination_in_degrees) <= range

    def calculate_distance(self, origin_in_degrees, destination_in_degrees):
        """
        Given some GPS coordinates, calculate the distance
        between 2 points. Uses the Haversine formula.

        As dataset grows, it might be more beneficial to use
        a quicker estimate formula such as the equirectangular
        distance approximation

        Args:
            origin (dict): origin GPS coordinates
            destination (dict): Destination GPS coordinates

        Returns:
            int: Distance(in km) from origin to destination
        """

        # Convert data to radians
        origin_in_radians = self.convert_gps_coordinates_to_radians(origin_in_degrees)
        destination_in_radians = self.convert_gps_coordinates_to_radians(destination_in_degrees)

        origin_lat = origin_in_radians["latitude"]
        origin_lon = origin_in_radians["longitude"]
        dest_lat = destination_in_radians["latitude"]
        dest_lon = destination_in_radians["longitude"]
        # Compute the distance between the origin and destination
        _logger.debug(f"Computing distance between lat: {origin_lat}, lon: {origin_lon} and lat: {dest_lat}, lon: {dest_lon}")
        delta_lon = dest_lon - origin_lon
        delta_lat = dest_lat - origin_lat
        a = sin(delta_lat / 2) ** 2 + cos(origin_lat) * cos(dest_lat) * sin(delta_lon / 2) ** 2
        c = 2 * asin(min(1, sqrt(a)))
        distance = EARTH_RADIUS_IN_KM * c

        return round(distance, 5)

    def convert_gps_coordinates_to_radians(self, gps_coordinates):
        """
        Convert a set of gps coordinates from degrees to radians

        Args:
             gps_coordinates (dict): A dictionary containing gps coordinates

        Returns:
            Dict: A dictionary of GPS coordinates converted to radians
        """
        latitude = self.degrees_to_radians(gps_coordinates['latitude'])
        longitude = self.degrees_to_radians(gps_coordinates['longitude'])

        return {"latitude": latitude, "longitude": longitude}

    def degrees_to_radians(self, degrees):
        """
        Function to convert degrees to radians. Round to 7 decimal places

        Args:
            degrees: Degrees
        """
        _logger.debug(f"Converting {degrees} degrees to radians")
        return round(float(degrees) * (pi / 180), 5)
