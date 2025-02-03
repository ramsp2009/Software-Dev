name = input("What is your name? ")
amount = eval(input("How many times do you want to print it? "))
#Eval can be swapped for int
for i in range (amount+1):
    print(name)