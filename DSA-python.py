#-------------------- Stack -----------------------------
class stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = stack()

#-------------------- Queue ---------------------

class Queue(object):

    def __init__(self):
        self.items = []

    def IsEmpty(self):
        return self.items == []

    def Enque(self,item):
        self.items.insert(0,item)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
