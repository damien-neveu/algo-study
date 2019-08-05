
class FenwickTree:

    tree = []

    def __init__(self, size=0, original_tree=[]):
        if len(original_tree) == 0:
            self.tree = [0 for i in range(size)]
        else:
            self.tree = [0 for i in range(len(original_tree))]
            for i, v in enumerate(original_tree):
                self.add(i, v)

    def sum(self, r):
        if r < 0 or r >= len(self.tree):
            return 0
        else:
            res = 0
            while r >= 0:
                res += self.tree[r]
                r = (r & (r+1)) - 1
            return res

    def add(self, i, delta):
        if 0 <= i < len(self.tree):
            while i < len(self.tree):
                self.tree[i] += delta
                i = i | (i+1)
