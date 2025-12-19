__all__ = ['greet', 'greetName', 'greetInteract']

def greet():
    print("Hi")

def greetName(name):
    greeting = "Hello"
    final = prepGreeting(greeting, name)
    print(final)

def prepGreeting(greeting, name):
    return f"{greeting} {name}!!"

def greetInteract():
    greeting = "Hi"
    name = input("Name: ")
    final = prepGreeting(greeting, name)
    print(final)

def Test():
    greet()
    greetName("Kiran")
    # greetInteract()

# Test()

# print(globals())
print(f"{__name__ = }")

if __name__ == '__main__':
    Test()