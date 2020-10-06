from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.max_size = capacity
        self.linked_list = None
        self.first_node = None
        self.last_node = None

    def get(self, key: int) -> int:
        if key in self.dict.keys():
            node = self.dict[key]
            self.move_to_front(node)
            # self.print_linked_list()
            return node.value
        else:
            # self.print_linked_list()
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict.keys():
            self.dict[key].value = value
            self.move_to_front(self.dict[key])
            # self.print_linked_list()
        else:
            n = self.insert_in_front(key, value)
            self.dict[key] = n
            if len(self.dict) > self.max_size:
                rm_n = self.remove_last()
                del self.dict[rm_n.key]
            # self.print_linked_list()

    def print_linked_list(self):
        print(" -> ".join(self.linked_list_to_arr()))

    def linked_list_to_arr(self):
        arr = []
        if self.first_node:
            current_node = self.first_node
            while current_node:
                arr.append("({},{})".format(current_node.key, current_node.value))
                current_node = current_node.nex
        return arr

    def move_to_front(self, n) -> None:
        if n is not self.first_node:
            if n is self.last_node:
                self.last_node = n.prev
            n.prev.nex = n.nex
            if n.nex:
                n.nex.prev = n.prev
            n.prev = None
            self.first_node.prev = n
            n.nex = self.first_node
            self.first_node = n

    def remove_last(self):
        rm_node = self.last_node
        if self.first_node is self.last_node:
            self.first_node = None
            self.last_node = None
        else:
            new_last_node = self.last_node.prev
            new_last_node.nex = None
            self.last_node = new_last_node
        return rm_node

    def insert_in_front(self, k, v):
        n = Node(k, v)
        if not self.dict:
            self.first_node = n
            self.last_node = n
        else:
            new_first_node = n
            new_first_node.nex = self.first_node
            self.first_node.prev = new_first_node
            self.first_node = new_first_node
        return n


class Node:

    def __init__(self, k: int, v: int, prev=None, nex=None):
        self.key = k
        self.value = v
        self.prev = prev
        self.nex = nex

    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
