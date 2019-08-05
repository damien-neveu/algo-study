
class Aggr:

    def __init__(self, floor=None, ceiling=None):
        self.floor = floor
        self.ceiling = ceiling

    def is_complete(self):
        return self.floor is not None and self.ceiling is not None

    def get(self):
        if self.is_complete():
            return self.floor, self.ceiling
        else:
            return None


def find_floor_and_ceiling(v, bst):
    if bst is None:
        return None
    else:
        return search_floor_and_ceiling(v, bst, Aggr())


def search_floor_and_ceiling(v, bst, aggr):
    if bst is None:
        return aggr.get()
    elif bst.data < v:
        aggr.floor = bst.data
        return search_floor_and_ceiling(v, bst.right, aggr)
    elif bst.data > v:
        aggr.ceiling = bst.data
        return search_floor_and_ceiling(v, bst.left, aggr)
    else:
        return bst.data, bst.data
