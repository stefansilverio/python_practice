import csv

with open("novel.csv", "r") as f:
    r = csv.reader(f, delimiter=",")  # converting novel file to a csv
    for row in r:
        print(", ".join(row))
