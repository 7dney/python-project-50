"""Parsing and open files."""

import argparse


def parser_arg():
    """Parsing arguments."""
    parser = argparse.ArgumentParser(description='Compares two configuration \
        files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='output format (default: "stylish")')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format