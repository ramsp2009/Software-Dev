year = int(input("Enter a year: "))
sum = 0
for i in range(1600,year):
    if i%4 == 0 and (i%100 != 0 or i%400 == 0):
       sum = sum + 1 

print(sum)

# I counted from 1600 - 2000 and im pretty sure its right