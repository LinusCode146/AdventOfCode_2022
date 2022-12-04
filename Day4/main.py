import csv
from pprint import pprint

pairs = []
total_overlapping = 0

def get_pairs():
    with open('information.txt') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            pairs.append(line)


def is_overlapping(pairs):
    overlap = 0
    for pair in pairs:
        first, second = pair
        first_splitted = first.split('-')
        second_splittedd = second.split('-')
        first_range = list(range(int(first_splitted[0]), int(first_splitted[1]) + 1))
        second_range = list(range(int(second_splittedd[0]), int(second_splittedd[1]) + 1))
        for item in first_range:
            if second_range.count(item) > 0:
                overlap += 1
                break
    return overlap


get_pairs()

pprint(is_overlapping(pairs))
