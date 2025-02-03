hour = int(input("Enter an hour: "))
time = int(input("Is it am (1) or pm (2)?"))
time_ahead = int(input("How far ahead? "))

if time == 2:
    if hour != 12:
        mhour = hour+12
    else:
        mhour = hour
else:
    if hour == 12:
        mhour = 0
    else:
        mhour = hour
mhour = mhour + time_ahead

am_pm = "am"
if mhour%24 > 11:
    am_pm = "pm"

mhour = mhour%24
mhour = mhour%12
print(mhour, am_pm)