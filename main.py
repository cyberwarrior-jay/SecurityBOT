import time
from builtins import print

ist = ["admin"]
psk = ["root"]
app = ["add name", "remove" , "print list"]
count = 0
c = "rough"
print("--------Welcome to Aniket Residence-------------\n")
# print("Please tell your name :  ")
name = "li"
while name != "exit" and count < 3:
    name = input("\nWhat is your name?: ")
    if name == ist[0]:
        cc = input("Enter password ? :")
        if cc == psk[0]:
            print("Welcome admin,")
            a = input("Please tell me what can i do for you: ")
            if a == app[0]:
                while c != "Bye":
                    c = str(input("\nName please: "))
                    if c != "Bye":
                        ist.append(c)
                        print(ist)

                print("Logging off as admin")
                time.sleep(5)
            elif a == app[1]:
                c = "abc"
                while c != "Bye":
                    c = str(input("\nSay Name to remove it : "))
                    if c != "Bye":
                        ist.remove(c)
                        print(ist)

                print("Logging off as admin")
                time.sleep(5)
            elif a == app[2]:
                print(ist)
                print("Logging off as admin")
                time.sleep(5)
            else:
                print("Welcome to Home")
                exit(0)
        else:
            print("Password is incorrect")
    elif name in ist:
        print(name + ",You are Welcome in House")
        exit(0)
    elif name == "exit":
        exit(0)
    else:
        print("You are unauthorized to enter the resident")
        print("Please try again in 10 sec \n")
        time.sleep(10)
        count += 1

print("\n\nNo. Of Trial count reached Maximum.You are blocked by the System")
print("Contact admin for further use")
exit(0)
