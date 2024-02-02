import itertools
import bingo
import numpy as np
import re
from pprint import pprint
from statistics import mode, multimode


def pairwise(iterable):
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def triplets(iterable):
    "s -> (s0, s1, s2), (s1, s2, s3), (s2, s3, s4), ..."
    a, b, c = itertools.tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)

def day1():
    f = open("aoc2021/1.in", "r")
    lines = f.readlines()
    f.close()
    pairs = pairwise([int(x) for x in lines])
    print(sum(1 for x in pairs if x[0] < x[1]))
    triplet = triplets([int(x) for x in lines])
    pairs = pairwise([sum(x) for x in triplet])
    print(sum(1 for x in pairs if x[0] < x[1]))

def day2():
    f = open("aoc2021/2.in", "r")
    lines = f.readlines()
    f.close()
    horizontal = 0
    vertical = 0
    depth = 0
    for line in lines:
        directions = line.split(' ')
        match directions[0]:
            case "forward":
                horizontal += int(directions[1])
                depth += vertical*int(directions[1])
            case "up":
                vertical -= int(directions[1])
            case "down":
                vertical += int(directions[1])
    print(horizontal*vertical)
    print(horizontal*depth)

def day3():
    f = open("aoc2021/3.in", "r")
    lines = f.readlines()
    f.close()
    gamma = ''
    bitlength = len(lines[1].strip())
    for i in range(bitlength):
        gamma += mode([x[i] for x in lines])
    print((0b111111111111 - int(gamma,2))*int(gamma,2))

    """verify the life support rating, 
    which can be determined by multiplying the oxygen generator rating 
    by the CO2 scrubber rating."""
    o2 = [x.strip() for x in lines]
    co2 = [x.strip() for x in lines]
    bitpoint = 0
    while len(o2) > 1:
        modal_digit = max(multimode(x[bitpoint] for x in o2))
        o2[:] = [item for item in o2 if item[bitpoint] == modal_digit]
        bitpoint += 1
    bitpoint = 0
    while len(co2) > 1:
        modal_digit = max(multimode(x[bitpoint] for x in co2))
        least_digit = '1' if modal_digit == '0' else '0'
        co2[:] = [item for item in co2 if item[bitpoint] == least_digit]
        bitpoint += 1
    
    print(int(o2[0],2)*int(co2[0],2))

def day4():
    f = open("aoc2021/4.in", "r")
    lines = f.readlines()
    f.close()

    bingo_balls = [int(x) for x in lines[0].strip().split(',')]
    card = []
    bingo_cards = []
    winners = []
    for line in lines[2:]:
        line = line.strip()
        if line == "":
            """about to get next bingo card, so process this one"""
            bingo_cards.append(bingo.Bingo(card))
            card.clear()
        else:
            """These numbers go with the current set"""
            card.append([int(x) for x in line.split()])
    for ball in bingo_balls:
        for bcard in bingo_cards:
            if bcard.is_winner():
                continue
            if all(bc.is_winner() for bc in bingo_cards) is True:
                return
            bcard.add_called(ball)
            if bcard.is_winner():
                winners.append(bcard.get_sum_unused()*ball)
    print(winners[0], winners[-1])

def day5():
    file = open("aoc2021/5.in", "r")
    lines = file.readlines()
    file.close()
    max_x = 0
    max_y = 0
    coords = []
    for line in lines:
        coords.append([int(x) for x in re.findall("(\d+)", line)])
        max_x = max(max(coords[-1][0::2]), max_x)
        max_y = max(max(coords[-1][1::2]), max_y)
    grid = np.tile(0, (max_y+1, max_x+1))
    for coord_list in coords:
        if coord_list[0] == coord_list[2]:
            #vertical line
            y1 = min(coord_list[1::2])
            y2 = max(coord_list[1::2]) + 1
            for y in range(y1,y2):
                grid[y][coord_list[0]] += 1
        elif coord_list[1] == coord_list[3]:
            #horizontal line
            x1 = min(coord_list[::2])
            x2 = max(coord_list[::2]) + 1
            for x in range(x1,x2):
                grid[coord_list[1]][x] += 1
        else:
            #diagonal - ignore for part 1
            x1 = coord_list[0]
            y1 = coord_list[1]
            x2 = coord_list[2]
            y2 = coord_list[3]

            m = (y2-y1)//(x2-x1)
            print(m)

            # y-y1=(y2-y1)/(x2-x1) (x-x1)
            if x1 > x2:
                step = -1
                diff = -1
            else:
                step = 1
                diff = 1
            for x in range(x1,x2+diff, step):
                y = m*(x-x1)+y1
                grid[y][x] += 1
    pprint(grid)
    print((grid >= 2).sum())



if __name__ == "__main__":
    day5()

    