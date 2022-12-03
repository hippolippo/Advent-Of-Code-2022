from os import path
with open(path.join(path.dirname(__file__), "input.txt"), "r") as file:
    lines = file.readlines()

top = -1
tid = -1
ida = 0
acc = 0
for line in lines:
    line = line[:-1]
    if line == "":
        if acc > top:
            top = acc
            tid = ida
        acc = 0
        ida += 1
    else:
        acc += int(line)
if acc > top:
    top = acc
    tid = ida
print(tid)
print(top)