import csv

with open("novel.csv", "w", newline='') as smoke:
    gump = csv.writer(smoke, delimiter=",")
    gump.writerow(["One, Two", 3])
    gump.writerow([4, 5, 6])
