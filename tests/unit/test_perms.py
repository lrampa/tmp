import pytest

from gokart_positions import permutations

# def test():
#     for i in permutations('ABCD', 4):
#         print(i)

def test_nojump_2():
    expected = [('A', 'B'), ('B', 'A')]
    perms = list(permutations('AB', 2))
    assert len(perms) == len(expected)
    for i in range(len(perms)):
        assert perms[i] == expected[i]

def test_nojump_3():
    expected = [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
    perms = list(permutations('ABC', 3))
    assert len(perms) == len(expected)
    for i in range(len(perms)):
        assert perms[i] == expected[i]

def test_jump_3_1():
    expected = [('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
    perms = list(permutations('ABC', jump=1))
    assert len(perms) == len(expected)
    for i in range(len(perms)):
        assert perms[i] == expected[i]

def test_jump_3_2():
    expected = [('C', 'A', 'B'), ('C', 'B', 'A')]
    perms = list(permutations('ABC', jump=2))
    assert len(perms) == len(expected)
    for i in range(len(perms)):
        assert perms[i] == expected[i]
