r = input("do you like to go to the beach?")

with open("writtentofile.txt", "w") as y:
    y.write(r)
