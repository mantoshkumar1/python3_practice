"""
Every Iterator object has three necessary characteristics.
  1. They have __next__ function.
  2. __next__ function returns values and finally throws StopIteration.
  3. They have __iter__ function which refers to self.
"""


# ------------------------ Example -------------------------------- #
class MyIterClass:
    def __init__(self):
        self.n = 0
        self.val = [10, 20, 30]
    
    def __next__(self):
        while self.n < len(self.val):
            i = self.n
            self.n += 1
            return self.val[i]
        
        raise StopIteration
    
    def __iter__(self):
        return self


# Usage of MyIterClass
a = MyIterClass()
while True:
    try:
        print(a.__next__(), end=" ")
    except StopIteration:
        print()
        break

"""
Generator: The generator is the elegant brother of iterator.txt that allows you to write
iterators like the one you saw earlier, but in a much easier syntax where you do not
have to write classes with __iter__() and __next__() methods.

yield basically replaces the return statement of a function but rather provides a
result to its caller without destroying local variables. Thus, in the next iteration,
it can work on this local variable value again. So unlike a normal function, where
on each call it starts with new set of variables - a generator will resume the
execution where it was left off.

lazy factory is a concept behind the generator and the iterator.txt. Which means they are
idle until you ask it for a value. Only when asked is when they get to work and produce
a single value, after which it turns idle again. This is a good approach to work with
lots of data. If you do not require all the data at once and hence no need to load all
the data in the memory, you can use a generator or an iterator.txt which will pass you each
piece of data at a time.

With Python2, a generator can use a return statement, but 'only without' a return
value - (almost) equivalent to raising StopIteration

Note that return isn't always equivalent to raising StopIteration: the difference
lies in how enclosing try/except constructs are treated. For example,

>>> def f1():
...     try:
...         return
...     except:
...        yield 1
>>> print list(f1())
[]
because, as in any function, return simply exits, but

>>> def f2():
...     try:
...         raise StopIteration
...     except:
...         yield 42
>>> print list(f2())
[42]
"""


# Generator Example #
def gen(start, end):
    while start <= end:
        yield start
        start += 1
    
    # at the end of loop, generator automatically raises StopIteration  # (or even return
    # statement causes StopIteration to be raised)


a = gen(1, 5)
while 1:
    try:
        print(a.__next__())
    except StopIteration:
        break
