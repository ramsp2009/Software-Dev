num = 1
num2 = 1
repeats = eval(input("How many Fibonacci numbers do you want to print? "))
print(num,  num2, end=',',sep=',')
for i in range(repeats+1):
    num = num + num2
    num2 = num + num2
    print(num, num2,sep=',', end=',')