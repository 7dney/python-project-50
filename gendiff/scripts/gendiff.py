#!/usr/bin/env python3

from gendiff.generate_diff import generate_diff
from gendiff.tools.argparse import parser_arg


def main():
    path_file1, path_file2, format_name = parser_arg()
    result = generate_diff(path_file1, path_file2, format_name)
    print(result)


if __name__ == '__main__':
    main()