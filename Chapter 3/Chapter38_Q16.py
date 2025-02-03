year = int(input("Year: "))
century = (year // 100)
m = (15 + century - ((century / 4) // 1) - (((8 * century + 13)/25) // 1)) % 30
n = (4 + century - ((century / 4) // 1)) % 7
a = (year % 4)
b = (year % 7)
c = (year % 19)
d = (19 * c + m) % 30
e = (2 * a + 4 * b + 6 *d + n) % 7

march = int(22 + d + e)
april = int(d+e-9)
if d == 29 and e == 6:
    april = 19
elif d == 28 and e == 6 and m in [2, 5, 10, 13, 16, 21, 24, 39]:
    april = 18
if  0 < april < 30:
    print("In ", year, ", Easter falls on April ", april)
elif 0 < march < 31:
    print("In ", year, ", Easter falls on March ", march)

