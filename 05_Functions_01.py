#region Declarations (Define Earlier vs Higher)

# def Bar():
#     print("Bar")
#     Baz()

# def Foo():
#     print("Foo")
#     Bar()

# def Baz():
#     print("Baz")

# def Main():
#     print("Main")
#     Foo()

# Main()

#endregion

#region Arg Passing

# def func_a():
#     pass

# def func_b():
#     pass

# def add(a:int, b:int)->int:
#     print(a)
#     print(b)
#     sum = a + b
#     # return 0
#     return sum

# print(add(1, 2))

# print(add("Hi", "there"))

# print(add(func_a, func_b))

# def add(a, b, c=0):
#     print(f"{a = }")
#     print(f"{b = }")
#     print(f"{c = }")
#     return a + b + c

# print(add(1, 2))    # Positional arguments

# print(add(b = 1, a = 2)) # Named Arguments

# print(add(1, 2, 3))     # Uses the Default arg in the definition

# ## Collections
# # List - Tuple
# # Set - FrozenSet
# # dictionary - NamedTuple
# # tuple
# # frozenset
# # namedtuple 

# i = 10; print(i); print(f"{ id(i) = }")
# i += 1; print(i); print(f"{ id(i) = }")
# i = 20; print(i); print(f"{ id(i) = }")

# s1 = "Test"; print(s1)
# s1 = "Best"; print(s1)
# print(s1[0])
# # s1[0] = "R"   # Error: tries to modify an immutable


# def PrintData(data):
#     # for x in data:
#     #     print(x, end=" - ")
#     while len(data) > 0:
#         print(data.pop(), end="-")
#     print()

# lst1 = [1, 2, 3, 4, 5]
# lst2 = [1, 2, 3, 4, 5]
# tup = tuple(lst2)

# PrintData(lst1[:])
# PrintData(lst1[:])
# # PrintData(tup)

# lst3 = lst1
# lst4 = lst1[:]

# print(f"{type(lst1) = }, {id(lst1) = }")
# print(f"{type(lst3) = }, {id(lst3) = }")
# print(f"{type(lst4) = }, {id(lst4) = }")


#####################################################

# lst1 = [1, 2, 3, 4, 5]
# # a = lst1[0]
# # b = lst1[1]
# # c = lst1[2]

# a, *b, c = lst1      # Unpacking lst1, packing extras into 'b'
# print(a, b, c)


# def add(a, b, c=0):
#     return a + b + c


# lst2 = [1, 2, 3]
# print(add(*lst2))




# def add(a, b, *data):                       # Iterative
#     # print(f"{type(data) = }, {data}")
#     sum = a + b
#     for val in data:
#         sum += val
#     return sum

# def add(*data):                             # Recursive
#     if not data:
#         return 0
#     return data[0] + add(*data[1:])

# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4))
# print(add(1, 2, 3, 4, 5))




# def PrintEmp(ceo, cto, **others):
#     print(f"{type(others)}, {others}")
#     print(f"{ceo = }, {cto = }", end=',')
#     for k, v in others.items():
#         print(f"{k}={v}", end=',')
#     print()
#     print

# PrintEmp(ceo="Rakesh", cto="Manish")
# PrintEmp(ceo="Rakesh", cto="Manish", cfo="Abhijeet")



# # def func(a, b, c):
# #     print(a, b, c, sep='')

# # func(10, 20, 30)

# def func(*vargs, **kwargs):
#     pass

# func(1, 2)
# func(1, 2, a=3, b=5)

#endregion