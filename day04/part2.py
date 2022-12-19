assignments = lambda assignment : tuple(int(x) for x in assignment.split('-'))

total = 0

with open('input.txt') as f:

    for pair in f.read().splitlines():
        elf1, elf2 = pair.split(',')
        elf1, elf2 = assignments(elf1), assignments(elf2)

        total += int(elf1[1] >= elf2[0] and elf2[1] >= elf1[0])

print(total)
