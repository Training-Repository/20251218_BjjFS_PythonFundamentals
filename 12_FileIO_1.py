import sys, os

def sys_demo():
    print(sys.path)
    print(sys.version)
    print(f"{sys.argv = }")

# sys_demo()

def os_demo():
    current_dir = os.getcwd()
    print(current_dir)

    new_dir = os.path.join(current_dir, "demo_dir")
    print(new_dir)

    if os.path.exists(new_dir):
        print("Folder already exists")
    else:
        os.makedirs(new_dir)
        print(f"Created - {new_dir}")
    
    print(os.listdir(current_dir))

    new_file = os.path.join(new_dir, "demo_file.txt")
    # file = open(new_file, "w")
    # file.write("This is a demo file")
    # file.close()

    # try:
    #     file = open(new_file, "w")
    #     file.write("This is a demo file")
    #     # file.close()
    # except Exception:
    #     # file.close()
    #     print("In exception handler")
    # finally:
    #     file.close()

    with open(new_file, "w") as file:
        file.write("This is a demo file")
    
    with open(new_file) as file:
        data = file.read()
        print(f"{data = }")

        s1 = "Content of the file is - {}"
        print(s1.format(data))
    
    os.remove(new_file)

    os.rmdir(new_dir)


os_demo()