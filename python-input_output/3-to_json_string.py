#!/usr/bin/python3
"""Module that returns the JSON representation of an object (string)."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a Python object as a string."""
    return json.dumps(my_obj)
