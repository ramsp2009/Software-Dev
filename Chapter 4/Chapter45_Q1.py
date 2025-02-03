cent = eval(input("Enter a cm value: "))
if cent < 0:
    print("Enter a a positive value: ")
else:
    inches = cent/2.54
    print(inches)