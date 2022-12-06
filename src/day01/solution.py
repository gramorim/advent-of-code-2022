#from ..util import read_file
from functools import reduce

def main():
    with open('input') as file:
        top_elves = find_top_elves(file)
        print(top_elves)
        print(f'sum: {reduce(lambda a, b: a+b, top_elves)}')

def find_top_elves(file):
    all_elves = calculate_all_elves(file)
    all_elves.sort()
    return (all_elves.pop(), all_elves.pop(), all_elves.pop())

def calculate_all_elves(file):
    all_elves = []
    current_elf = 0
    for line in file.readlines():
        if not line.startswith('\n'):
            current_elf += int(line)
        else:
            all_elves.append(current_elf)
            current_elf = 0
    return all_elves

main()