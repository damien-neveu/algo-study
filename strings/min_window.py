import math

# Question 2
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n)
# https://leetcode.com/problems/minimum-window-substring/

# minWindow("ADOBECODEBANC", "ABC"); // -> BANC
# minWindow("ADObEcODEBANC", "Abc"); // -> ADObEc

max_unicode_basic_latin_chars = 126


def min_window(st, pat):
    # print("min_window({}, {})".format(st, pat))
    target_count = len(pat)
    if target_count == 0:
        return ""
    elif target_count > len(st):
        return None
    hash_pat = build_hash(pat)
    hash_str = build_hash()
    count, current_start_index, start_index, min_length = 0, 0, 0, math.inf
    for i in range(0, len(st)):
        s_unicode = ord(st[i])
        hash_str[s_unicode] += 1
        if hash_pat[s_unicode] > 0 and hash_pat[s_unicode] >= hash_str[s_unicode]:
            count += 1
        if count == target_count:
            while count == target_count and current_start_index < i:
                c_unicode = ord(st[current_start_index])
                hash_str[c_unicode] -= 1
                if hash_pat[c_unicode] > 0 and hash_str[c_unicode] < hash_pat[c_unicode]:
                    count -= 1
                    candidate_min_length = i - current_start_index + 1
                    # print("i={}, candidate_min_length={}".format(str(i), str(candidate_min_length)))
                    if candidate_min_length < min_length:
                        min_length = candidate_min_length
                        start_index = current_start_index
                        # print("min_length={}, start_index={}".format(str(min_length), str(start_index)))
                current_start_index += 1
            # print("after while: start_index={}, current_start_index={}, count={}".format(
            #     str(start_index), str(current_start_index), str(count)))
    if min_length == math.inf:
        return None
    return st[start_index:start_index+min_length]


def build_hash(st=""):
    hsh = [0] * max_unicode_basic_latin_chars
    for s in st:
        hsh[ord(s)] += 1
    return hsh

