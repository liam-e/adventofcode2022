beats = { 1: 3, 2: 1, 3: 2 }

decode = {
    'A': 1, 'B': 2, 'C': 3,
    'X': 1, 'Y': 2, 'Z': 3,
}

def score(round):
    opponent, me = round.split(' ')
    opponent, me = decode[opponent], decode[me]

    if beats[me] == opponent: # win
        return me + 6
    elif me == opponent: # draw
        return me + 3
    else: # loss
        return me

total = 0

with open('input.txt') as f:
    for round in f.read().splitlines():
        total += score(round)

print(total)
