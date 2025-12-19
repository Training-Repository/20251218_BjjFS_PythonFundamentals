from multipledispatch import dispatch

@dispatch(int, int)
def add(a:int, b:int)->int:
    print("Integer -->", a + b)

@dispatch(float, float)
def add(a:float, b:float)->float:
    print("Float -->", a + b)

@dispatch(str, str)
def add(a:str, b:str)->str:
    print("String -->", a + b)

add(1, 2)
add(1.1, 2.2)
add("One", "Two")

# def add1(a:int, b:int)->int:
#     print("Integer1 -->", a + b)

# # def add(a:float, b:int)->int:
# #     print("Integer2 -->", a + b)

# # def add(a:int, b:float)->int:
# #     print("Integer3 -->", a + b)

# def add2(a:int, b:int, c:int)->int:
#     print("Integer4 -->", a + b + c)


# def add(*args):
#     match len(args):
#         case 2:
#             add1(*args)
#         case 3:
#             add2(*args)





# #--------------------
# add(1, 2)
# # add(1.1, 2)
# # add(1, 2.2)
# add(1, 2, 3)
