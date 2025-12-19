x = ["manish", "abhijeet", "rakesh", "vinayak", "shankar"]
y = []
## MAP 
resMap = list(map(str.capitalize,x))
print(type(resMap), resMap)

for val in x:
    y.append(str.capitalize(val))

print(f"{y = }")


## Filter
def HasR(word):
    if 'r' in str.lower(word):
        return True
    else:
        return False

resFilter = list(filter(HasR, x))
print(resFilter)


## Reduce

def Add(a, b):
    return a + b

from functools import reduce
resRed = reduce(Add, x)
print(resRed)

##################################
# print(dir(int))

# p = 10
# print(p)
# print(str(p))
# print(p.__str__())
# print(p.__repr__())

# class Test:
#     def __init__(self):
#         self.x = 10

#     def __str__(self):
#         return f"Data --> {self.x}"
    
# t = Test()
# print(t.__str__())
# print(t.__repr__())