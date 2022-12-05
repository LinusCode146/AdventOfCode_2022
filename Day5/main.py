from pprint import pprint


stacks = {
    '1': ['J', 'F', 'C', 'N', 'D', 'B', 'W'],
    '2': ['T', 'S', 'L', 'Q', 'V', 'Z', 'P'],
    '3': ['T', 'J', 'G', 'B', 'Z', 'P'],
    '4': ['C', 'H', 'B', 'Z', 'J', 'L', 'T', 'D'],
    '5': ['S', 'J', 'B', 'V', 'G'],
    '6': ['Q', 'S', 'P'],
    '7': ['N', 'P', 'M', 'L', 'F', 'D', 'V', 'B'],
    '8': ['R', 'L', 'D', 'B', 'F', 'M', 'S', 'P'],
    '9': ['R', 'T', 'D', 'V']
}

lines = [line.rstrip().split() for line in open('info.in')]

for item in lines:
    f = item[3]
    t = item[5]
    for times in range(int(item[1])):
        element = stacks[f].pop(0)
        stacks[t].insert(0, element)

solution = ''
for key, value in stacks.items():
    solution += value[0]
print(solution)