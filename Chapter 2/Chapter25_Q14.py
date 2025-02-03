rows = int(input ("Enter the height of the diamond: "))
height = 0
if rows % 2 == 0:
    print ("Please enter an odd number.")
else:
    height = rows // 2 +1
for i in range(height):
    print(" " * (height - i - 1) + "*" * (2 * i + 1))
for i in range(height - 2, -1, -1):
    print(" " * (height - i - 1) + "*" * (2 * i + 1))