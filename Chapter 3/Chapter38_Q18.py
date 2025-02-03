change = int(input("Enter an amount of change in pennies: "))

if format == "D":
    change = (change * 100)
elif format == "P":
    change = change

quarters = change // 25
change = change % 25
dimes = change // 10
change = change % 10
nickels = change // 5
change = change % 5
pennies = change

print(quarters, "quarters,", dimes, "dimes,", nickels, "nickels,", pennies, "pennies" )

#I had to search up how much a nickel was cuz of this :imp: