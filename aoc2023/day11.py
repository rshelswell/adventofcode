import numpy as np

def day11a():
    file11 = open("aoc2023/day11.input")
    Lines = file11.readlines()
    file11.close()
    data = []
    for line in Lines:
        data.append([i for i in line.strip()])
        if all(i == "." for i in line.strip()):
            data.append(['.' for i in line.strip()])
    # print(data)
    data = np.array(data).transpose()
    # print(data)
    universe = []
    for line in data:
        universe.append(line)
        if all(i == "." for i in line):
            universe.append(['.' for i in line])
    galaxies = []
    for x, line in enumerate(universe):
        locs = [y for y, i in enumerate(line) if i == "#"]
        galaxies.extend([(x,y) for y in locs])
    print(galaxies)
    total = 0
    for i, gal in enumerate(galaxies):
        for gal2 in galaxies[i+1:]:
            total += abs(gal[0]-gal2[0]) + abs(gal[1]-gal2[1])
    print(total)

def day11b():
    file11 = open("aoc2023/day11.input")
    Lines = file11.readlines()
    file11.close()
    data = []
    blank_cols = []
    for l, line in enumerate(Lines):
        data.append([i for i in line.strip()])
        if all(i == "." for i in line.strip()):
            blank_cols.append(l)
    # print(data)
    data = np.array(data).transpose()
    # print(data)
    universe = []
    blank_rows = []
    for l, line in enumerate(data):
        universe.append(line)
        if all(i == "." for i in line):
            blank_rows.append(l)
    galaxies = []
    for x, line in enumerate(universe):
        locs = [y for y, i in enumerate(line) if i == "#"]
        galaxies.extend([(x,y) for y in locs])
    print(galaxies)
    total = 0
    for i, gal in enumerate(galaxies):
        for gal2 in galaxies[i+1:]:
            total += abs(gal[0]-gal2[0]) + abs(gal[1]-gal2[1])
    print(total)


if __name__ == "__main__":
    day11a()