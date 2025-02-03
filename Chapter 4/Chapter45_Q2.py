temp = eval(input("Enter a temperature: "))
unit = input("What unit was it in (Celcius or Fahrenheit): ")

if unit == "Celsius" or "celsius":
    temp = temp*9/5 +32
    print(temp, " is the Fahrenheit equivalent")
elif unit == "Fahrenheit" or "fahrenheit":
    temp = (temp-32)*5/9
    print(temp, " is the Celsius equivalent")
else:
    print("Uh oh invalid unit type: ")