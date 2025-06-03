#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file."""

import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing list if file exists, else start with an empty list
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Append new arguments
items.extend(sys.argv[1:])

# Save updated list back to file
save_to_json_file(items, filename)
