class queue:
    def __init__(self):
        self.queue = list()

    def addtoq(self, dataval):
        if dataval not in self.queue:
          self.queue.insert(0, dataval)

    # Pop method to remove element
    def removefromq(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue!")

    def size(self):
        return len(self.queue)


