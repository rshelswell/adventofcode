from pprint import pprint


def day10a():
    file10 = open("aoc2023/day10ex.input")
    Lines = file10.readlines()
    tubemap = []
    checked = []
    for y, line in enumerate(Lines):
        tubemap.append(line.strip())
        checked.append([False for i in line.strip()])
        if "S" in tubemap[-1]:
            startpoint = (line.find("S"), y)
    pprint(tubemap)
    pprint(checked)
    pprint(f"Starting at {startpoint}")
    max_x = len(tubemap[0]) - 1
    max_y = len(tubemap) - 1
    pprint(f"Bottom corner at ({max_x}, {max_y})")

    currentpoint = startpoint
    if not checked[currentpoint[1]][currentpoint[0]]:
        pass
        

if __name__ == "__main__":
    day10a()