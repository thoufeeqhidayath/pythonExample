
class stack:
    def __init__(self):
        self.stack = []

    def push(self, dataval):
            self.stack.append(dataval)

    # Use list pop method to remove element
    def pop(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

