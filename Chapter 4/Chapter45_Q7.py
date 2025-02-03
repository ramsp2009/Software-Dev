num1 = eval(input("Enter a number: "))
num2 = eval(input("Enter a number: "))
if num1-num2 <=0.001 and num2-num1 <= 0.001:
    print("Numbers are close")
else:
    print("Numbers are not close")