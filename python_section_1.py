from typing import Dict, List
from collections import defaultdict
from typing import Dict, Any
from itertools import permutations
import re
import polyline
import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2

import pandas as pd


def reverse_by_n_elements(lst: List[int], n: int) -> List[int]:
    """
    Reverses the input list by groups of n elements.
    """
    # Your code goes here.
    for i in range(0, len(lst), n):
        # Reverse the sublist from i to i+n
        lst[i:i+n] = reversed(lst[i:i+n])
    return lst


def reverse_groups(lst, n):
    # Iterate through the list in steps of 'n'
    for i in range(0, len(lst), n):
        # Reverse the sublist from i to i+n
        lst[i:i+n] = reversed(lst[i:i+n])
    return lst

# Input
input_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3

# Output
output_list = reverse_by_n_elements(input_list, n)
print(output_list)
   


def group_by_length(lst: List[str]) -> Dict[int, List[str]]:
    """
    Groups the strings by their length and returns a dictionary.
    """
    # Your code here
    length_dict = defaultdict(list)

    # Iterate over each word in the input list
    for word in lst:
        # Add the word to the list corresponding to its length
        length_dict[len(word)].append(word)

    # Sort the dictionary by key (length of the words) and return it
    return dict(sorted(length_dict.items()))
input_words = ["apple", "bat", "car", "elephant", "dog", "bear"]

# Output
output_dict = group_by_length(input_words)
print(output_dict)

def flatten_dict(nested_dict: Dict[str, Any], sep: str = '.') -> Dict[str, Any]:
    def _flatten(d: Dict[str, Any], parent_key: str = '') -> Dict[str, Any]:
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(_flatten(v, new_key).items())
            elif isinstance(v, list):
                for i, item in enumerate(v):
                    items.extend(_flatten(item, f"{new_key}[{i}]").items())
            else:
                items.append((new_key, v))
        return dict(items)

    return _flatten(nested_dict)
input_dict = {
    "road": {
        "name": "Highway 1",
        "length": 350,
        "sections": [
            {
                "id": 1,
                "condition": {
                    "pavement": "good",
                    "traffic": "moderate"
                }
            }
        ]
    }
}

# Output
output_dict = flatten_dict(input_dict)
print(output_dict)

def unique_permutations(nums: List[int]) -> List[List[int]]:
    # Use set to filter out duplicate permutations
    return [list(p) for p in set(permutations(nums))]

# Input
input_nums = [1, 1, 2]

# Output
output_permutations = unique_permutations(input_nums)
print(output_permutations)

def find_all_dates(text: str) -> List[str]:
    date_pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b|\b\d{4}\.\d{2}\.\d{2}\b'

    # Find all matching dates
    return re.findall(date_pattern, text)
input_text = "I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23."

# Output
output_dates = find_all_dates(input_text)
print(output_dates)


def polyline_to_dataframe(polyline_str: str) -> pd.DataFrame:
    """
    Converts a polyline string into a DataFrame with latitude, longitude, and distance between consecutive points.
    
    Args:
        polyline_str (str): The encoded polyline string.

    Returns:
        pd.DataFrame: A DataFrame containing latitude, longitude, and distance in meters.
    """
    return pd.Dataframe()


def haversine(lat1, lon1, lat2, lon2):
    # Radius of Earth in meters
    R = 6371000
    # Convert latitude and longitude from degrees to radians
    lat1_rad, lon1_rad = radians(lat1), radians(lon1)
    lat2_rad, lon2_rad = radians(lat2), radians(lon2)

    # Differences
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula
    a = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Distance in meters
    distance = R * c
    return distance


# Function to decode polyline and calculate distances


def time_check(df) -> pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
