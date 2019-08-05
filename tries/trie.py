ENDS_HERE = '#'


class Trie:

    def __init__(self):
        self._trie = {}

    def insert(self, string):
        trie = self._trie
        for char in string:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[ENDS_HERE] = True

    def find(self, prefix):
        trie = self._trie
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return []
        return self._postfixes(trie)

    def _postfixes(self, t):
        arr = []
        for c, subtrie in t.items():
            strings = ['']
            if c is not ENDS_HERE:
                strings = list(map(lambda p: c + p, self._postfixes(subtrie)))
            arr.extend(strings)
        return arr

