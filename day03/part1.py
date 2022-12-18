from string import ascii_letters

priority = {item: priority for priority, item in enumerate(ascii_letters, start=1)}

total = 0

for rucksack in open('input.txt').read().splitlines():
    num_items = len(rucksack)
    compartment1, compartment2 = rucksack[:num_items//2], rucksack[num_items//2:]
    common_item = list(set(compartment1).intersection(compartment2))[0]
    total += priority[common_item]

print(total)
