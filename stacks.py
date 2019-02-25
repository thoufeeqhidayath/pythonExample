class stack:
    def __init__(self):
        self.items=list()

    def push(self,item):
        if item not in self.items:
            self.items.insert(0,item)



    def pop(self):
        length=len(self.items)-1
        lid=self.items[length]
        self.items.remove(lid)
        return lid


    def size(self):
        return len(self.items)
