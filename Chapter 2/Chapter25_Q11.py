wide = eval(input("How wide is the box? "))
tall = eval(input("How tall is the box? "))

for i in range(1):
    print("*"*wide)

for i in range(tall-2):
    print("*", " "*(wide-2), "*",sep="")

for i in range(1):
    print("*"*wide)