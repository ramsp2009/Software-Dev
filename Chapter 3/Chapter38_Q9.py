hour = int(input("Enter hour: "))
future = int(input("How many hours ahead: "))
final = hour+future
print(final%12, "o'clock")