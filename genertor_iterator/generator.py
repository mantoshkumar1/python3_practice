def counter(maximum):
    i = 1
    while i < maximum:
        val = (yield i)  # val will hold the yielded value that will be used next time
        print('i={}, val={}'.format(i, val))
        # If value provided, change counter
        if val is not None:  # catches the value sent through 'send' function
            i += val
        else:  # if next is used, then val comes as None [ next(gen) is effectively equivalent to cr.send(None) ]
            i += 1


it = counter(10)
# print(it.send(30)) # Throws error: TypeError: can't send non-None value to a just-started generator
print(next(it))  # 1   (advance to the yield statement, otherwise can't call send)
print(next(it))  # 2
print(it.send(3))  # 5
print(it.send(5))

'''
Output:
-------
1
i=1, val=None
2
i=2, val=3
5
i=5, val=5
Traceback (most recent call last):
  File "main.py", line 18, in <module>
    print(it.send(5))
StopIteration
'''

(yield i) works like a bi-directional channel. 'yield i' sends the next val and 'yield' part waits for receiving value.
    If next is called, then 'yield' receives None and if 'send' is used then it receives the sent value.


    def controlled_execution():
        set
        things
        up
        try:
            yield thing
        finally:
            tear
            things
            down


    for thing in controlled_execution():  Q: does this call next or create multiple gen obj?
        do
        something
        with thing


