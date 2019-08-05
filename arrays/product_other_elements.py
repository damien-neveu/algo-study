import operator
import functools


def product_other_elements(arr):
    res = []
    for index, elem in enumerate(arr):
        if index == 0:
            res.append(product(arr[1:]))
        else:
            res.append(mul_and_div(res[index-1], arr[index-1], elem))
    return res


def product_other_elements_no_divide(arr):
    res = []
    prefixes = build_prefixes(arr)
    suffixes = build_suffixes(arr)
    for i, element in enumerate(arr):
        res.append(prefixes[i] * suffixes[i])
    return res


def product(xs):
    return functools.reduce(operator.mul, xs, 1)


def build_prefixes(arr):
    res = []
    for i, elem in enumerate(arr):
        if i == 0:
            res.append(1)
        else:
            res.append(product(arr[:i]))
    return res


def build_suffixes(arr):
    res = []
    for i, elem in enumerate(arr):
        if i == len(arr)-1:
            res.append(1)
        else:
            res.append(product(arr[i+1:]))
    return res


def mul_and_div(previous_product, previous_element, current_element):
    return previous_product * previous_element / current_element
