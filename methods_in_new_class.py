# http://www.java2s.com/Tutorials/Python/Class/Overload_len_method_for_len_function.htm
# http://farmdev.com/src/secrets/magicmethod/index.html#introducing-getitem


class NewClass:
    def __init__(self):
        self.arr = [10, 20]
    
    def __repr__(self):
        "It must return string type ONLY"
        return "object created"
    
    """
    DO NOT USE THESE MAGIC FUNCTIONS - YOU ARE NOT MAGICIAN BUT MERELY A PROGRAMMER WHO IS STILL
    AFRAID OF APPROACHING A WOMAN. GOT IT!
    
    http://farmdev.com/src/secrets/magicmethod/index.html#introducing-getitem
    
    Implementing __getitem__ in a class allows its instances to use the [] (indexer) operators.
    
    def __getitem__(self, item):
        pass
    
    def __setitem__(self, key, value):
        pass
    
    def __delitem__(self, key):
        pass
    
    Implementing __getattr__ overrides Python's default mechanism for member access.
    Example: a.x
    
    def __getattr__(self, item): #?
        return self.arr
    
    def __setattr__(self, key, value):
        pass
    
    def __delattr__(self, item):
        pass
    
    def __contains__(self, item):
        pass
    
    def __index__(self):
        pass
    
    def __add__(self, other):
        pass
    """
    
    def __len__(self):
        return len(self.arr)
    
    ### These below 6 special methods are used to compare objs of same type ###
    # These overloaded comparison operators must return BOOLEAN #
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
