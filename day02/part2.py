win = { 3: 1, 1: 2, 2: 3 }
loss = { 1: 3, 2: 1, 3: 2 }

decode = {
    'A': 1, 'B': 2, 'C': 3,
    'X': 1, 'Y': 2, 'Z': 3,
}

def score(round):
    opponent, outcome = round.split(' ')
    opponent, outcome = decode[opponent], decode[outcome]

    if outcome == 1: # lose
        return loss[opponent]
    elif outcome == 2: # draw
        return opponent + 3
    else: # win
        return win[opponent] + 6

total = 0

with open('input.txt') as f:
    for round in f.read().splitlines():
        total += score(round)

print(total)
