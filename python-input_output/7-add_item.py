#!/usr/bin/python3
"""Script that adds all arguments to a Python list,
and then saves them to a file in JSON format.
"""

import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])  # Add all arguments except the script name
save_to_json_file(items, filename)
