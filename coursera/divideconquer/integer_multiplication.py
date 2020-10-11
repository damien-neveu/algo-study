from typing import Tuple


def karatsuba(i1: int, i2: int) -> int:
    si1, si2 = convert_to_evenly_long_strings(i1, i2)
    length = len(si1)
    if length <= 2:
        return i1 * i2
    a, b, c, d = int(si1[0:length//2]), int(si1[length//2:]), int(si2[0:length//2]), int(si2[length//2:])
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd
    print("10**{} * {} + 10**{} * {} + {}".format(length, ac, length//2, ad_bc, bd))
    return 10**length * ac + 10**(length//2) * ad_bc + bd


def convert_to_evenly_long_strings(i1: int, i2: int) -> Tuple[str, str]:
    si1, si2 = str(i1), str(i2)
    max_length = max(len(si1), len(si2))
    max_length = max_length + 1 if max_length % 2 == 1 else max_length
    return si1.rjust(max_length, '0'), si2.rjust(max_length, '0')
