* ***enumerate*** is a built-in function of Python. This method adds
 counter to an iterable and returns an enumerate object.
The syntax of **enumerate()** is:\
`enumerate(iterable, start=0)`
    - **iterable**: A sequence, an iterator, or objects that *supports
     iteration*.
    - **start** (optional): enumerate() starts counting from this number
    . Default value = 0
 * Note: Both parameters of ***enumerate*** could be both positional or
  keyword arguments.
```python
# Explanation for allowance of both positional or keyword arguments
some_list = ['a', 'b']
# Then all of them are valid syntax and will provide same output content
# in a for loop except fourth example.
enumerate(some_list, 10)
enumerate(iterable=some_list, start=10)
enumerate(some_list, start=10)

# SyntaxError: positional argument follows keyword argument
# enumerate(iterable=some_list, 10) 
```

* The enumerate object yields pairs containing a count (from start, which
 defaults to zero) and a value yielded by the iterable argument. enumerate is
 useful for obtaining an indexed list:\
`[ (0, seq[0]), (1, seq[1]), (2, seq[2]), ... ] `

* It allows us to loop over something and have an automatic counter.
```python
some_list = ['a', 'b']
for counter, value in enumerate(some_list):
    print(counter, value)

# output:
# 0 a
# 1 b
```
* ***enumerate*** also accepts an optional argument which makes it even more
 useful.
 ```python
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

# Output:
# 1 apple
# 2 banana
# 3 grapes
# 4 pear
```
* The optional argument allows us to tell ***enumerate*** from where to start
the index. You can also create tuples containing the index and list item using
a list. Here is an example:
```python
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
# Output: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]
```
* You can convert enumerate objects to list and tuple using *list()* and
 *tuple()* method respectively.
```python
e = enumerate(['a', 'b', 'b'])
list(e) # output: [(0, 'a'), (1, 'b'), (2, 'b')]

e = enumerate(['a', 'b', 'b'])
set(e) # output: {(1, 'b'), (0, 'a'), (2, 'b')}
# For the set(e) output: A set is an unordered collection of elements without
# duplicate entries. When printed, iterated or converted into a sequence, its
# elements will appear in an arbitrary order.
```

* ***enumerate*** is a **generator** as it has both the `__next__` and
 `__iter__` methods. Thus, once an enumerator is consumed, it will throw
  `StopIteration` exception (`for` loop handles this exception gracefully).
```python
e = enumerate(['a', 'b'])
list(e) # output: [(0, 'a'), (1, 'b')]
list(e) # output: []
```

###### References:
1. https://book.pythontips.com/en/latest/enumerate.html
2. https://www.programiz.com/python-programming/methods/built-in/enumerate
