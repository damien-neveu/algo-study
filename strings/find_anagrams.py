from collections import Counter

def find_anagrams_brute(w, s):
    res = []
    reversed_w = w[::-1]
    for (i, c) in enumerate(s):
        substr = s[i:i + len(w)]
        if substr == w or substr == reversed_w:
            res.append(i)
    return res


def find_anagrams(w, s):
    if len(w) == 0 or len(s) == 0 or len(w) > len(s):
        return []
    else:
        counter_w = Counter(w)
        res = []
        current_counter = Counter(s[:len(w)])
        if counter_w == current_counter:
            res.append(0)
        for i in range(len(w), len(s)):
            c = s[i]
            decrease_occurence(s[i - len(w)], current_counter)
            increase_occurence(c, current_counter)
            if counter_w == current_counter:
                res.append(i - len(w) + 1)
        return res


def decrease_occurence(char, dictio):
    existing_count = dictio[char]
    if existing_count == 1:
        del dictio[char]
    elif existing_count > 1:
        dictio[char] = existing_count - 1


def increase_occurence(char, dictio):
    existing_count = dictio[char]
    if existing_count is None:
        dictio[char] = 1
    else:
        dictio[char] = existing_count + 1

