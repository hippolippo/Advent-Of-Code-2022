from os import path
with open(path.join(path.dirname(__file__), "input.txt"), "r") as file:
    lines = file.readlines()

for line in lines:
    line = line[:-1]
    #...

print()