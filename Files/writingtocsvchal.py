import csv

with open("bubble.csv", "w", newline='') as t:
    o = csv.writer(t, delimiter=",")
    o.writerow(["top gun", "risky business," "minority report"])
    o.writerow(["training day", "man on fire", "flight"])
