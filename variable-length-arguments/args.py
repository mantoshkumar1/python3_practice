def func(*args):
    print(args)
    print(*args)

a = [1, 2, 3]

# here "a" is passed as tuple of list: ([1, 2, 3],)
func(a)
# print(args) -> ([1, 2, 3],)
# print(*args) -> [1, 2, 3]

# here "a" is passed as tuple of integers: (1, 2, 3)
func(*a)
# print(args) -> (1, 2, 3)
# print(*args) -> 1 2 3

