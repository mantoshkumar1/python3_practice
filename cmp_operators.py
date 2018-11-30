import heapq


class Item:
    def __init__(self, i, s):
        self.i = i
        self.s = s
    
    def __eq__(self, other):
        return self.i == other.i and self.s == other.s
    
    def __nq__(self, other):
        return self.i != other.i or self.s != other.s
    
    def __gt__(self, other):
        if self.i == other.i:
            return self.s < other.s
        return self.i > other.i
    
    def __ge__(self, other):
        if self.i == other.i:
            return self.s <= other.s
        return self.i >= other.i
    
    def __lt__(self, other):
        if self.i == other.i:
            return self.s > other.s
        return self.i < other.i
    
    def __ge__(self, other):
        if self.i == other.i:
            return self.s >= other.s
        return self.i <= other.i
    
    def __str__(self):
        return "%d - %s\n" % (self.i, self.s)


class A:
    def __init__(self):
        self.arr = []
    
    def insert(self, i, s):
        print("inserted: %d - %s" % (i, s))
        heapq.heappush(self.arr, Item(i, s))
    
    def min(self):
        return self.arr[0]


a = A()

a.insert(4, 'e')
print(a.min())

a.insert(3, 'd')
print(a.min())

a.insert(4, 'f')
print(a.min())

a.insert(2, 'a')
print(a.min())

a.insert(2, 'b')
print(a.min())

a.insert(1, 'a')
print(a.min())
