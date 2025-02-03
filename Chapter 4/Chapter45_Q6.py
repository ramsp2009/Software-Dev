items = int(input("How many items are you buying? "))

if items < 10:
    print(items*12)
elif items < 100:
    print(items*10)
elif items >= 100:
    print(items*7)
else:
    print("Invalid number of items...")