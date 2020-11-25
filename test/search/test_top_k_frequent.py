import pytest
from search.top_k_frequent import Solution

sol = Solution()


def test_single_element_list():
    nums = [5]
    assert sol.topKFrequent(nums, 1) == nums


def test_larger_list():
    nums = [12, 8, 9, 12, 5, 7, 3, 9, 12, 3, 3, 0, 5, 2, 3, 3]
    expected_answer = [3, 12, 9, 5]
    assert set(sol.topKFrequent(nums, 4)) ^ set(expected_answer) == set()


# PYTHONPATH=. pytest test/search/ -v -s
