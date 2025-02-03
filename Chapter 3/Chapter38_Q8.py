seconds = input("Seconds: ")

remainder = int(seconds)%60
minutes = int(seconds)//60
print(minutes, "minutes", remainder, "seconds")