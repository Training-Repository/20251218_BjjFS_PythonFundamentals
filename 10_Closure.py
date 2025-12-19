# def wrapper(x):
#     def inner():
#         print(x)
#     return inner

# fn1 = wrapper(10)
# fn2 = wrapper(20)
# print("-"*20)

# fn1()
# fn2()


#######################################

def power_of(power):
    def inner(val):
        return val**power
    return inner

square = power_of(2)
cube = power_of(3)
print("-"*20)

print(square(10))
print(cube(10))

# def power(val, power):
#     return val**power

# print(power(10, 2))

# def square(val):
#     power = 2
#     return val**power

# print(square(10))
