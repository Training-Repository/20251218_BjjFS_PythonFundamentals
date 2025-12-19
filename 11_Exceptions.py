# st = Stack(10)
# st.push(1)
# .
# .
# .
# st.push(10)
# # st.push(11)

# st.pop()
# st.pop()
# .
# .
# .
# .
# st.pop() # 1
# st.pop() # -999: Stack Empty

#############################################################

from random import randint

def Bar():
    print("Bar")
    # res = 10/0
    if randint(0, 1):
        # raise ValueError("That's not a value we accept here!!")
        raise IndexError("This index not longer exists")
        # raise KeyError("This index not longer exists")
    print("Return Bar")

def Foo():
    print("Foo")
    try:
        Bar()
    except (ZeroDivisionError, ValueError) as  ex:
        print(f"EXCEPTION(ZD, VE) --> {type(ex)}", ex)
    except Exception as ex:
        print(f"EXCEPTION (EX) --> {ex!r}")
        raise

    print("Return Foo")

def Main():
    print("Main")
    try:
        Foo()
    except IndexError as ex:
        # print(f"EXCEPTION --> {ex.__repr__()}")
        print(f"EXCEPTION (IE) --> {ex!r}")
    
    print("Return Main")

Main()