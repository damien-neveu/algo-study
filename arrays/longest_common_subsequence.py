# Longest Common Subsequence

# Challenge
# O(n x m) time and memory.

# longestCommonSubsequence([3, 9, 8, 3, 9, 7, 9, 7, 0], [3, 3, 9, 9, 9, 1, 7, 2, 0, 6]); // -> [ 3, 3, 9, 9, 7, 0 ]


def longest_common_subsequence(a, b, res=[]):
    if len(b) == 0:
        return res
    n = b[0]
    newB = b[1:]
    for v in a:

