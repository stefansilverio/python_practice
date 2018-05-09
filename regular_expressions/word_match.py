import re

line = "The ghost that says boo haunts the loo."


t = re.findall(".oo",
               line)


print(t)


# any word that starts with any character and followed by oo's
# re.findall("__*oo__")
