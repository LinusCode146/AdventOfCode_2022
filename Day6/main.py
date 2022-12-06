from pprint import pprint


def all_different(x):
    x = list(x)
    for char in x:
        if x.count(char) > 1:
            return False
    return True
        

code = ''
for line in [line.rstrip().split() for line in open('info.in')]:
    code += line[0]

solution = []

length = 14 # make it 4 for part 1


for idx, char in enumerate(list(code)):
    if all_different(code[idx:idx+length]):
        solution.append(idx+length)

quiz_answer = solution[0]