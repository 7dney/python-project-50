"""Test generate_diff"""

import pytest
from gendiff.generate_diff import generate_diff
from pathlib import Path


@pytest.mark.parametrize(
    "file1,file2,right_answer,format_name",
    [
        ('file1.json', 'file2.json', 'right_answer_stylish.txt', 'stylish'),
        ('file1.yml', 'file2.yml', 'right_answer_stylish.txt', 'stylish'),
        ('file1.json', 'file2.json', 'right_answer_plain.txt', 'plain'),
        ('file1.yml', 'file2.yml', 'right_answer_plain.txt', 'plain'),
        ('file1.json', 'file2.json', 'right_answer.json', 'json'),
        ('file1.yml', 'file2.yml', 'right_answer.json', 'json')
    ]
)
def test_diff_stylish_json(file1, file2, right_answer, format_name):
    path_dict1 = get_fixture_path(file1)
    path_dict2 = get_fixture_path(file2)
    path_right_answer = get_fixture_path(right_answer)
    with open('{}'.format(path_right_answer)) as f:
        right_answer = f.read()[:-1]
    assert generate_diff(path_dict1, path_dict2, format_name) == right_answer
    if format_name == 'stylish':
        assert generate_diff(path_dict1, path_dict2) == right_answer


def get_fixture_path(file_name):
    return Path(Path(__file__).parent.absolute() / 'fixtures' / file_name)