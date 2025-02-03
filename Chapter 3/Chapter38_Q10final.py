power = int(input("Power: "))
number_digits=int(input("Number of digits to be found: "))
digit = 2**power
mod_needed = 10**number_digits
last_digit = digit%mod_needed
print(last_digit)

