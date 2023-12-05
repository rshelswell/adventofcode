import re

def day5a():
    file5 = open(r'aoc2023/day5ex.input', 'r')
    Lines = file5.readlines()
    file5.close()
    seeds = []
    for line in Lines:
        if len(seeds) == 0:
            seeds = [int(i) for i in re.findall(r'(\d+)', line)]
    print(seeds)
    return 0
        