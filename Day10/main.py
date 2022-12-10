from pprint import pprint
from functools import reduce

lines = [line.rstrip().split() for line in open('info.in')]
pprint(lines)
cycles = 0
x = 1
total_sum = []
milestones = [20, 60, 100, 140, 180, 220]
for idx, line in enumerate(lines):
    if line[0] == 'noop':
        cycles += 1
        if cycles in milestones:
            print(cycles)
            total_sum.append(x * cycles)

    if line[0] == 'addx':
        for i in range(2):
            cycles += 1
            if cycles in milestones:
                print(cycles)
                total_sum.append(x * cycles)
        x += int(line[1])
print(sum(total_sum))
        
