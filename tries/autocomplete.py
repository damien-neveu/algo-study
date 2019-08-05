from tries.trie import Trie


def autocomplete(prefix, words):
    if len(prefix) is 0:
        return []
    trie = Trie()
    for word in words:
        trie.insert(word)
    postfixes = trie.find(prefix)
    return list(map(lambda p: prefix + p, postfixes))
