from itertools import count
import sys
"""
count(start=0, step=1)
Return a count object whose .__next__() method returns consecutive values which is equivalent to:

  def count(start=0, step=1):
     x = start
     while True:
         yield x
         x += step
"""
itr_obj = count(start=10, step=2)

for i in range(5):
    print(itr_obj.__next__(), end=' ', file=sys.stdout)

