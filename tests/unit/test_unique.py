import pytest

from gokart_positions import is_unique_arr

def test_answer():
    all_perms = [[1,2], [2,1]]
    assert is_unique_arr(all_perms) == True

def test_unique_duplicate():
    all_perms = [[1,2], [1,2]]
    assert is_unique_arr(all_perms) == False


def test_unique_duplicate_three_levels():
    all_perms = [[1,2,3], [2,3,1], [1,2,3]]
    assert is_unique_arr(all_perms) == False

def test_unique_duplicate_three_levels_unique():
    all_perms = [[1,2,3], [2,3,1], [3,1,2]]
    assert is_unique_arr(all_perms) == True

def test_unique_duplicate_long():
    all_perms = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    ]
    assert is_unique_arr(all_perms) == False
