from pprint import pprint
from functools import reduce
import math

inspected = [0,0,0,0,0,0,0,0]
ROUNDS = 20
lines = [line.rstrip().split() for line in open('info.in')]
lines = list(filter(lambda x: x != [], lines))

monkeys = {
    0: [92, 73, 86, 83, 65, 51, 55, 93],
    1: [99, 67, 62, 61, 59, 98,],
    2: [81, 89, 56, 61, 99],
    3: [97, 74, 68],
    4: [78, 73],
    5: [50],
    6: [95, 88, 53, 75],
    7: [50, 77, 98, 85, 94, 56, 89]
}


operations = [line[1:] for line in lines if line[0] == 'Operation:']
directions = [lines[idx:idx+3] for idx, line in enumerate(lines) if line[0] == 'Test:']

def change_worry_level(operation, current):
    if operation[3] == '*':
        if operation[4] == 'old': return current * current
        return current * int(operation[4])
    elif operation[3] == '+':
        return current + int(operation[4])

def next_monkey(divisible, is_true, is_false, item):
    if item % divisible == 0:
        return is_true
    else:
        return is_false


for round in range(ROUNDS):
    print(round)
    for key, inventory in monkeys.items():
        inspected[key] += len(inventory)
        for idx, item in enumerate(inventory):
            new_item = math.floor(change_worry_level(operations[key], item) / 3) #!divide by three because you are relieved
            new_monkey = next_monkey(int(directions[key][0][-1]), int(directions[key][1][-1]), int(directions[key][2][-1]), new_item)
            monkeys[new_monkey].append(new_item)
        monkeys[key] = []
            

print(348*347)



