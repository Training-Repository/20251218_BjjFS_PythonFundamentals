# def Square(x):
#     return x**2

# def Cube(x):
#     return x**2


# Square = lambda x: x**2

Toolkit = [lambda x: x**2, lambda x: x**3, lambda x: x**4]

for fn in Toolkit:
    print(fn(10))

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
l3 = [10, 20, 30]
tup = (l1, l2, l3)
print(type(tup))
print(tup)
tup[0].append(4)
print(tup)
tup1 = (1, 2, 3, 4)
tup[0] = 9