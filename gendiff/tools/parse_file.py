"""Parsing the file"""

import json
import yaml
from pathlib import Path


def get_dict_from_file(path_file):
    """Parse the file and return dict"""
    file_extension = Path(path_file).suffix
    return open_file(path_file, file_extension)


def open_file(path_file, file_extension):
    if file_extension.lower() == '.json':
        with open(path_file) as f:
            return json.load(f)
    elif file_extension.lower() == '.yml' or file_extension.lower() == '.yaml':
        with open(path_file) as f:
            return yaml.safe_load(f)