
class MaxStack:

    def __init__(self):
        self.values = []
        self.maxes = []

    def push(self, value):
        self.values.append(value)
        if not self.maxes:
            self.maxes.append(value)
        else:
            self.maxes.append(max(self.maxes[-1], value))

    def pop(self):
        self.maxes.pop(-1)
        return self.values.pop(-1)

    def max(self):
        return self.maxes[-1]

