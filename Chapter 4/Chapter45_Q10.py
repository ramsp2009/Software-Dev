from random import randint
for i in range(10):
    num1 = randint(1,10)
    num2 = randint(1,10)
    answer = input("What is " + str(num1) + "x" + str(num2)+ " ")
    if int(answer) == num1*num2:
        print("Right.")
    else:
        print("Wrong the answer is", num1*num2)