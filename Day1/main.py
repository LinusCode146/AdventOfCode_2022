import csv
from pprint import pprint

calories = []

def get_calories():
    with open('information.txt') as file:
        reader = csv.reader(file)
        for line in reader:
            if line == []:
                calories.append(-50)
            else:
                calories.append(line[0])


def get_sums(calories):
    current_split = 0
    sums = []
    top_three = []
    for idx, item in enumerate(calories):
        if item == -50:
            sum_range = [int(a) for a in calories[current_split:idx]]
            sums.append(sum(sum_range))
            current_split = idx + 1
    for _ in range(3):
        top_three.append(max(sums))
        sums.remove(max(sums))
    print(sum(top_three))         

get_calories()
pprint(get_sums(calories))