from collections import deque


class LruCache:

    def __init__(self, n):
        self.max_size = n
        self.dictio = {}
        self.keys_in_order = deque()

    def set(self, key, value):
        if key not in self.dictio:
            self.keys_in_order.append(key)
        self.dictio[key] = value
        if len(self.dictio) > self.max_size:
            del self.dictio[self.keys_in_order.popleft()]

    def get(self, key):
        if key in self.dictio:
            return self.dictio[key]
        return None
