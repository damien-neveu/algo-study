import pytest

from coursera.divideconquer.count_inversions import sort_and_count_inversions


def test_small_array():
    (sorted_nums, num_inversions) = sort_and_count_inversions([1, 3, 5, 2, 4, 6])
    assert num_inversions == 3
    assert sorted_nums == [1, 2, 3, 4, 5, 6]


def test_file_input():
    nums = []
    with open('test/coursera/divideconquer/int.array.txt') as f:
        nums = [int(line.rstrip()) for line in f]
    (_, num_inversions) = sort_and_count_inversions(nums)
    assert num_inversions == 2407905288

