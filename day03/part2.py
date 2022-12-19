from string import ascii_letters
from itertools import islice

priority = {item: priority for priority, item in enumerate(ascii_letters, start=1)}

total = 0

with open('input.txt') as f:
    while rucksacks := list(islice(f, 3)):
        rucksack1, rucksack2, rucksack3 = [set(rucksack.strip()) for rucksack in rucksacks]
        common_item = list(rucksack1 & rucksack2 & rucksack3)[0]
        total += priority[common_item]

print(total)
