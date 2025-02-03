import math
for i in range(0,360,15):
    degrees = math.degrees(i)
    sin = round(math.sin(degrees),4)
    cos = round(math.cos(degrees), 4)
    print(i, (sin, cos) , sep="----")