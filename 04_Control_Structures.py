import os

# 1. Control Structures
a = 55
if a > 10:
    print("Greater")
elif a < 10:
    print("Lesser")
else:
    print("Equal")

# 2. Loop Constructs
## For

### Initialiser, Condition, Stepping
### for(i = 0; i < 10; i++)

for a in range(10):
    print(a, end=', ')
print()

srch = 17
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for a in lst:
    # print(a, end=', ')
    if a == srch:
        print(f"Found")
        break
else:
    print("Not Found")

## While

idx = len(lst)
# while idx >= 0:
while idx:
    if lst[idx] == srch:
        print("Found")
        break
    idx -= 1
else:
    print("Not Found")
## Do-While NOT supported in Python

# 3. Match Case
cs = 2
match cs:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Unclassfied")

