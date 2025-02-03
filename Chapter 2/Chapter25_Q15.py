height = int(input("How high do you want it "))
remainder = height%2 
betterheight = height-remainder

if height%2 == 0:
    print("I said ODD!")
    exit()

print(" "*(betterheight) + "*")

for i in range(int(betterheight/2)-1):
    print(" "*(betterheight-(i+1))+"*"+" "*(2*i+1)+"*")

print(" "*int((betterheight/2)-1), "*"*int(betterheight+1))

for i in range(int(betterheight/2)):
    print(" "*int((betterheight/2)-(i+1))+"*"+" "*int(((2*i+1)+((betterheight/2)+2) )),"*")