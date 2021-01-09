import os
names = ""

def check(name):
    global names
    if name+".txt" in os.listdir():
        try:
            name = name[0:len(name)-1] + str(int(name[-1])+1)
        except ValueError:
            name = name + "0"
        check(name)
    else:
        names = name
    
def menu():
    name = input("Name of the of the file:")
    check(name)
    with open(names+".txt", "w") as file:
        pass

if __name__ == "__main__":
    menu()


