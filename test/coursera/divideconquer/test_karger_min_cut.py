import pytest

from coursera.divideconquer.karger_min_cut import alg, to_adjacency_list, contract


def test_to_adjacency_list():
    graph = to_adjacency_list("test/coursera/divideconquer/karger.min.cut.small.txt")
    assert graph == {1: [2, 4], 2: [1, 3, 4], 3: [2, 4], 4: [1, 2, 3]}


def test_contract():
    graph = {1: [2, 4], 2: [1, 4, 4], 4: [1, 2, 2]}
    contract(graph, 4, 2)
    assert graph == {1: [4, 4], 4: [1, 1]}

# PYTHONPATH=. pytest test/coursera/ -v
