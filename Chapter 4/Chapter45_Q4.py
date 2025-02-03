credits = int(input("How many credits have you take? "))

if credits <= 23:
    print(" You are a Freshman")
elif credits <=53:
    print("You are a Sophomore")
elif credits <=83:
    print("You are a Junior")
elif credits >83:
    print("You are a senior")
else:
    print("Invalid number or something.")