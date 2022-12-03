from os import path
with open(path.join(path.dirname(__file__), "input.txt"), "r") as file:
    lines = file.readlines()

ROCK = 0
PAPER = 1
SCISSORS = 2

def compute_score(them, me):
    winScore = 0
    if them == me:
        winScore = 3
    elif (them+1)%3 == me:
        winScore = 6
    return winScore + me + 1

PLAYER_DEVIATION_MAP = {"X": -1, "Y": 0, "Z": 1}
ELF_INPUT_MAP = {"A": ROCK, "B": PAPER, "C": SCISSORS}

score = 0
for line in lines:
    line = line[:-1]
    them = ELF_INPUT_MAP[line[0]]
    deviation = PLAYER_DEVIATION_MAP[line[-1]]
    score += compute_score(them, (them+deviation)%3)

print(score)