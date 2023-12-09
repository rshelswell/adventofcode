
def direction_finder(dirs):
    length = len(dirs)
    index = 0

    while True:
        yield 0 if dirs[index] == "L" else 1
        index = (index + 1) % length

def day8a():
    file8 = open("aoc2023/day8.input", "r")
    Lines = file8.readlines()
    file8.close()
    mapping = dict()
    for i, line in enumerate(Lines):
        if i == 0:
            directions = line.strip()
            continue
        if i > 1:
            mapping.update({line[0:3]:(line[7:10], line[12:15])})
    # print(mapping)
    # print(directions)
    next_dir = direction_finder(directions)
    location = "AAA"
    steps = 0
    while location != "ZZZ":
        location = mapping[location][next(next_dir)]
        steps += 1
        print(location)
    print(steps)        


if __name__ == "__main__":
    day8a()