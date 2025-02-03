meal = int(input("Price of meal: "))
percent = int(input("Percent tip: "))
tip = meal * (percent/100)
total = tip + meal
print("Tip =", tip, "Total = ", total)