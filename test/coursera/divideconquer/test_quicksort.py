import pytest

from coursera.divideconquer.quicksort import quicksort, alg


@pytest.mark.skip(reason='no longer sorts the input array but rather counts comparisons')
def test_small_array():
    arr = [3, 8, 2, 5, 1, 4, 7, 6]
    quicksort(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8]


def test_large_array():
    counts_comparisons = alg('test/coursera/divideconquer/quick.sort.txt')
    assert len(counts_comparisons) == 3

# PYTHONPATH=. pytest test/coursera/ -v
