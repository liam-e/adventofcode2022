with open('input.txt') as f:
    crates, instructions = f.read().split('\n\n')

crates = crates.splitlines()
crates.reverse()

num_crates = int([x for x in crates[0].split(' ') if x.isnumeric()][-1])

stacks = [[] for _ in range(num_crates)]

for layer in crates[1:]:
    for i in range(0, num_crates):
        crate = layer[i*4+1:i*4+2]
        if crate != ' ':
            stacks[i].append(crate)

cratemover = []

for instruction in instructions.splitlines():
    amount, origin, destination = [int(x) for x in instruction.split(' ')[1::2]]

    for _ in range(amount):
        cratemover.append(stacks[origin-1].pop())
    
    for _ in range(amount):
        stacks[destination-1].append(cratemover.pop())

answer = ''
for stack in stacks:
    if len(stack) > 0:
        answer += stack[-1]

print(answer)