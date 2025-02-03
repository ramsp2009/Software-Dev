number = eval(input("Enter a number: "))
divisors = []
for i in range(number):
    if number%(i+1) == 0:
        divisors.append(i+1)

print(divisors)
    