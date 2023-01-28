"""
Exercise 4. ITMO Python course. Group 124-16.

REPK Console App

Date 27.11.2022

@author: ilia.ivanov@outlook.com
"""

import zip_util
import math
from geopy import distance

zip_codes = zip_util.read_zip_all()
# print(zip_codes)

def loc():
    """
    Gets ZIP Code from a user;
    Revokes function find_zip_code(zip_code);
    Revokes float_to_dms function to convert float coordinates to deg°min'sec"
    Prints results.
    :return:
    """
    zip_code = input("Enter a ZIP Code to lookup => ")
    location = find_zip_code(zip_code)
    lat = lambda location : f'N' if location[1] > 0 else f'S'
    long = lambda location : f'E' if location[1] > 0 else f'W'
    if isinstance(location, list):
        print(f"ZIP Code {location[0]} is in {', '.join(location[3:5])}, {location[5]} county,\n"
              f"coordinates: {float_to_dms(location[1])}{lat(location)}, "
              f"{float_to_dms(location[2])}{long(location)}")
    elif isinstance(location, str):
        print(location)

def find_zip_code(zip_code):
    """
    Finds data corresponding to ZIP Code in zip_util.read_zip_all()
    :param zip_code:
    :return:
    If ZIP Code exists in zip_util.read_zip_all(), returns data as a list
    otherwise return 'invalid' message.
    """
    flag = False
    for i in range(len(zip_codes) - 1):
        if zip_code == zip_codes[i][0]:
            flag = True
            return zip_codes[i]
    if not flag:
        return "Invalid or unknown ZIP Code"

def float_to_dms(coordinates):
	"""
	converts float angle to deg°min'sec"
	:param coordinates:
	:return: str[]
	"""
	return f"{abs(math.trunc(coordinates))}°{math.trunc(coordinates % 1 * 60)}'{round(abs((coordinates % 1) * 60 % 1 * 60), 2)}\""

def zip():
    """
    Find ZIP by City and State names
    :return:
    """
    flag = False
    city = input("Enter a city name to lookup => ").title()
    state = input("Enter the state name to lookup => ").upper()
    city_zips = []
    for i in range(len(zip_codes) - 1):
        if city == zip_codes[i][3] and state == zip_codes[i][4]:
            flag = True
            city_zips.append(zip_codes[i][0])
            print(f"The following ZIP Code(s) found for {city}, {state}:{', '.join(city_zips)}")
            return
    if not flag:
        print(f"No ZIP Code found for: {city}, {state}.")


def dist():
    """
    Calculates distance between two ZIP Code addresses
    :return:
    """
    zip_code_1 = input("Enter the first ZIP Code => ")
    zip_code_2 = input("Enter the second ZIP Code => ")
    location_1 = tuple(find_zip_code(zip_code_1)[1:3])
    location_2 = tuple(find_zip_code(zip_code_2)[1:3])
    if type(location_1[0]) == float and type(location_2[0]) == float:            #isinstance(location_1, tuple) and isinstance(location_2, tuple):
        distance_miles = round(distance.distance(location_1, location_2).miles, 2)
        print(f"The distance between {zip_code_1} and {zip_code_2} is {distance_miles} miles.")
        return
    else:
        print(f"The distance between {zip_code_1} and {zip_code_2} cannot be determined.")
