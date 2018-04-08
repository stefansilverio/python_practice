with open("writtentofile.py", "w") as written:
    written.write("Hi from Python!")

with open("writtentofile.py", "r") as written:
    print(written.read())

# You can only call read on a file once. Save in a container.

my_list = ["butter", "smoke"]
with open("writtentofile.py", "r") as written:
    my_list.append(written.read())

print(my_list)
