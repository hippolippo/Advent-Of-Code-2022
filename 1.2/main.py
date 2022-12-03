from os import path
with open(path.join(path.dirname(__file__), "input.txt"), "r") as file:
    lines = file.readlines()

scores = list()
ida = 0
acc = 0
for line in lines:
    line = line[:-1]
    if line == "":
        scores.append((ida, acc))
        acc = 0
        ida += 1
    else:
        acc += int(line)
if acc > 0:
    scores.append((ida, acc))
scores.sort(key=lambda a: -a[1])
print("1:", scores[0])
print("2:", scores[1])
print("3:", scores[2])
print(sum(score[1] for score in scores[:3]))