width = int(input("Width of rectangle: "))
height = int(input("Height of rectangle: "))
numbers = 0

for i in range(height):
    for x in range(width):
        print(numbers % 10, end=" ")
        numbers = numbers+1
    print()