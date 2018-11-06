# http://www.java2s.com/Tutorials/Python/Class/Overload_len_method_for_len_function.htm
# http://farmdev.com/src/secrets/magicmethod/index.html#introducing-getitem
class NewClass:
    def __init__(self):
        self.arr = [10, 20]
    
    def __repr__(self):
        return "object created"
    
    def __getitem__(self, item):
        pass
    
    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass
    
    def __getattr__(self, item): #?
        pass
    
    def __setattr__(self, key, value):
        pass
    
    def __delattr__(self, item):
        pass
        
    def __hash__(self):
        pass
        
    def __contains__(self, item):
        pass
        
    def __index__(self):
        pass
    
    def __add__(self, other):
        pass
    
    def __subtract__(self, other):  # why its not red
        pass
    
    def __sizeof__(self):
        pass
    
    def __len__(self):
        return len(self.arr)

    ### These below 6 special methods are used to compare objs of same type ###
    def __lt__(self, other):
        return self.arr < other.arr

    def __le__(self, other):
        return self.arr <= other.arr

    def __gt__(self, other):
        return self.arr > other.arr

    def __ge__(self, other):
        return self.arr >= other.arr

    def __eq__(self, other):
        return self.arr == other.arr

    def __ne__(self, other):
        return self.arr != other.arr


a = NewClass()
assert len(a.arr) == len(a)
