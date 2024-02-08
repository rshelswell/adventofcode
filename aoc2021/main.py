import itertools
import bingo
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import re
from collections import Counter, defaultdict
from functools import lru_cache
from math import prod
from pprint import pprint
from statistics import mode, multimode, median, median_high, median_low


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

def day6():
    file = open("aoc2021/test.in", "r")
    fish = np.array([int(x) for x in file.readline().strip().split(',')])
    file.close()
    
    for i in range(18):
        c = Counter(fish)[0]
        fish -= 1
        fish[fish == -1] = 6
        fish = np.append(fish,[8 for i in range(c)])

    print(len(fish))

def day6_2():
    file = open("aoc2021/6.in", "r")
    start_fish = [x for x in file.readline().strip().split(',')]
    file.close()
    fish = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for f in start_fish:
        fish[int(f)] += 1
    for i in range(256):
        new_fish = fish[0]
        for j in range(8):
            fish[j]=fish[j+1]
        fish[6] += new_fish
        fish[8] = new_fish
    print(sum(fish.values()))

def day7():
    file = open("aoc2021/7.in", "r")
    data = [int(x) for x in file.readline().split(",")]
    file.close()
    print(median(data), median_low(data), median_high(data))
    x = median(data)
    min_sum = sum([abs(d-x) for d in data])
    print(min_sum)

    min_sum = 10000000000
    for x in range(min(data), max(data)):
        min_sum = min((min_sum,sum([abs(d-x)*(abs(d-x)+1)/2 for d in data])))
    print(min_sum)

def day8():
    file = open("aoc2021/8.in", "r")
    lines = file.readlines()
    file.close()
    count = 0
    for line in lines:
        count += sum([1 for x in line.strip().split('|')[1].split() if len(x) in (2, 3, 4, 7)])
    print(count)
    count = 0
    for line in lines:
        patterns = line.strip().split("|")[0].split()
        values = line.strip().split("|")[1].split()
        patterns.sort(key=len)
        pattern_dict = dict()
        pattern_dict.update({'1': patterns[0]})
        pattern_dict.update({'7': patterns[1]})
        pattern_dict.update({'4': patterns[2]})
        pattern_dict.update({'8': patterns[9]})
        indices_90 = [i+6 for i, item in enumerate(patterns[6:9]) if all(c in item for c in pattern_dict['1'])]
        index_6 = np.setdiff1d([6,7,8], indices_90)[0]
        pattern_dict.update({'6': patterns[index_6]})
        index_9 = [i+6 for i, item in enumerate(patterns[6:9]) if all(c in item for c in pattern_dict['4'])][0]
        pattern_dict.update({'9': patterns[index_9]})
        pattern_dict.update({'0': patterns[np.setdiff1d(indices_90, [index_9])[0]]})
        index_3 = [i+3 for i, item in enumerate(patterns[3:6]) if all(c in item for c in pattern_dict['1'])][0]
        pattern_dict.update({'3': patterns[index_3]})
        index_5 = [i+3 for i, item in enumerate(patterns[3:6]) if all(c in pattern_dict['6'] for c in item)][0]
        pattern_dict.update({'5': patterns[index_5]})
        index_2 = np.setdiff1d([3,4,5],[index_5, index_3])[0]
        pattern_dict.update({'2': patterns[index_2]})
        digit = ''
        for value in values:
            digit += [key for key, val in pattern_dict.items() if set(value) == set(val)][0]
        count+=int(digit)
    print(count)

def day9():
    file = open("aoc2021/9.in", "r")
    lines = file.readlines()
    file.close()
    data = [line.strip() for line in lines]
    del lines
    height = len(data)
    width = len(data[0])
    risk = 0
    for h in range(height):
        for w in range(width):
            N=True
            E=True
            S=True
            W=True
            if h > 0:
                N = data[h][w] < data[h-1][w]
            if h < height - 1:
                S = data[h][w] < data[h+1][w]
            if w > 0:
                W = data[h][w] < data[h][w-1]
            if w < width - 1:
                E = data[h][w] < data[h][w+1]
            if all([N,E,S,W]):
                risk += 1 + int(data[h][w])
    print(risk)


    # Initialize the list of region sizes and the number of rows and columns
    sizes = []
 
    # Define a helper function that performs Depth First Search from a given cell
    def dfs(i, j):
        # Check if the cell is valid and has value 0
        if i < 0 or i >= height or j < 0 or j >= width or arr[i][j] != 0:
            return 0
        # Mark the cell as visited by setting it to 1
        arr[i][j] = 1
        # Recursively explore the four adjacent cells and add their sizes
        return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
    arr = []
    for d in data:
        intlist = [1 if x == 9 else 0 for x in list(map(int, d))]
        arr.append(intlist)
    arr = np.array(arr)

    # Loop through the 2D array and start DFS from each 0 cell
    for i in range(height):
        for j in range(width):
            if arr[i][j] == 0:
                # Get the size of the current region and append it to the list
                size = dfs(i, j)
                sizes.append(size)

    # Print the list of region sizes
    print(sorted(sizes))
    print(prod(sorted(sizes)[-3:]))
            
def day10():
    file = open("aoc2021/10.in", "r")
    lines = file.readlines()
    file.close()
    scores = {')': 3 , ']': 57, '}': 1197, '>': 25137}
    closes = {'(':')', '{':'}', '[':']', '<':'>'}
    illegals = 0
    incompletes = []
    for line in lines:
        corrupt = False
        entries = []
        for c in line.strip():
            if c in ('(', '[', '{', '<'):
                # open a chunk is always OK
                entries.append(c)
                
            elif c == closes[entries[-1]]:
                # chunk closed correctly
                entries.pop()
            else:
                corrupt = True
                illegals += scores[c]
            if corrupt:
                break
        if not corrupt:
            incompletes.append(entries)

    print(illegals)

    line_scores = []
    close_scores = {')': 1,']': 2, '}': 3,'>': 4}
    for incomplete in incompletes:
        ls = 0
        while incomplete:
            ls *= 5
            ls += close_scores[closes[incomplete.pop()]]
        line_scores.append(ls)


    print(median(line_scores))

def day11():
    file = open("aoc2021/11.in", "r")
    lines = file.readlines()
    file.close()
    data = np.array([int(x) for line in lines for x in line.strip()])
    data = np.reshape(data, (len(lines),-1))
    print(data)

    flashes = 0
    height = len(data)
    width = len(data[0])
    flashed = []
    counting = 0
    while len(flashed) < height*width:
        data += 1
        # get all octopuses with value > 9
        _10s = np.where(data > 9)
        flashed = []
        while len(_10s[0]):
            for y, x in zip(_10s[0], _10s[1]):
                if (x,y) in flashed:
                    # print(f"already checked {x},{y}")
                    continue
                else:
                    flashed.append((x,y))
                data[max(y-1,0):min(y+2,height), max(x-1,0):min(x+2,width)] += 1
                # print(data)
            _10s = np.where(data > 9)
            data = np.where(data<=9, data, -1000)
        flashes += len(flashed)
        data = np.where(data>0, data, 0)
        print(f"step: {counting}, flashes: {len(flashed)}, total flashes: {flashes}")
        counting += 1
    print(data)
    print(counting)

def day12():
    file = open("aoc2021/12.in", "r")
    lines = file.readlines()
    file.close()
    tunnels = {}
    visited = defaultdict()
    edges = []
    for line in lines:
        ends = line.strip().split("-")
        if ends[0] in tunnels:
            tunnels.update({ends[0]: tunnels[ends[0]] + [ends[1]]})
        else:
            tunnels.update({ends[0]:[ends[1]]})
            visited.update({ends[0]:0})
        if ends[1] in tunnels:
            tunnels.update({ends[1]: tunnels[ends[1]] + [ends[0]]})
        else:
            tunnels.update({ends[1]:[ends[0]]})
            visited.update({ends[1]:0})
        edges.append((ends[0], ends[1]))
    
    def find_routes(graph, start='start', end='end'):
        routes = []

        partial_routes = [(start, [start])]

        while partial_routes:
            node, path = partial_routes.pop(0)
            if node == end:
                routes.append(path)
            else:
                for neighbour in graph.neighbors(node):
                    if neighbour[0] == start or neighbour[0] == 'start':
                        continue
                    if neighbour[0].islower() and neighbour in path:
                        continue
                    partial_routes.append((neighbour, path + [neighbour]))

        return routes
        
    def find_routes_2(graph, start='start', end='end', route=[]):
        visited[start] += 1
        route.append(start)
        if start == end:
            #arrived
            yield route
        else:
            small_caves = len([item for item, count in Counter([i for i in route if i.islower()]).items() if count > 1])
            for node in graph.neighbors(start):
                if node == 'start':
                    continue
                if visited[node] == 0 or node.isupper() or visited[node] < 2 and small_caves == 0:
                    yield from find_routes_2(graph, node, end, route)
        route.pop()
        visited[start] -= 1

    
    G = nx.Graph()
    G.add_edges_from(edges)

    routes = find_routes(G)
    # print(routes)
    print(f"There are {len(routes)} routes")

    routes = find_routes_2(G)
    r_count = 0
    for r in routes:
        r_count += 1
        print(r_count, r)
    
def day13():
    file = open("aoc2021/13.in", "r")
    lines = file.readlines()
    file.close()

    dot_locations = set()
    fold_instructions = []

    for line in lines:
        if 0 < len(line.strip()) < 11:
            #it's a coordinate pair
            dot_locations.add(tuple(int(item) for item in line.strip().split(",")))
        elif len(line.strip()) > 11:
            #it's a folding instruction
            dir = line.strip()[11]
            loc = int(line.strip()[13:])
            fold_instructions.append((dir, loc))
    
    for axis, pos in fold_instructions:
        if axis == 'y':
            #points below pos will reflect upwards
            tmp_set = set()
            for dot in dot_locations:
                if dot[1] < pos:
                    tmp_set.add(dot)
                else:
                    dot_y = 2 * pos - dot[1]
                    tmp_set.add((dot[0], dot_y))
        elif axis == 'x':
            #points right of pos will reflect left
            tmp_set = set()
            for dot in dot_locations:
                if dot[0] < pos:
                    tmp_set.add(dot)
                else:
                    dot_x = 2 * pos - dot[0]
                    tmp_set.add((dot_x, dot[1]))
        dot_locations.clear()
        dot_locations = dot_locations.union(tmp_set)
        
        print(dot_locations)
        print(len(dot_locations))

    x = []
    y = []
    for x_i, y_i in dot_locations:
        x.append(x_i)
        y.append(-y_i)
    
    plt.style.use('_mpl-gallery')
    # plot
    fig, ax = plt.subplots()
    
    ax.scatter(x, y)

    ax.set(xlim=(0, 42), xticks=np.arange(1, 42),
        ylim=(-7, 1), yticks=np.arange(1, 7))

    plt.show()


def day14():
    file = open("aoc2021/14.in", "r")
    lines = file.readlines()
    file.close()
    polymer = lines.pop(0).strip()
    lines.pop(0)
    insertions = defaultdict()

    for line in lines:
        line = line.strip()
        insertions[line[0:2]] = line[-1]
    
    for i in range(10):
        new_polymer = ''
        for pair in itertools.pairwise(polymer):
            new_polymer += pair[0] + insertions[''.join(pair)]
        polymer = new_polymer + polymer[-1]
    
    print(len(polymer))
    cnt = Counter(polymer)
    most = cnt.most_common(1)
    least = cnt.most_common()[-1]
    print(most[0][1]-least[1])

def day14_2():
    file = open("aoc2021/14.in", "r")
    lines = file.readlines()
    file.close()
    polymer = lines.pop(0).strip()
    lines.pop(0)
    insertions = defaultdict(str)
    pairs = defaultdict(int)
    letters = dict()

    for pair in itertools.pairwise(polymer):
        pairs[''.join(pair)] += 1

    for line in lines:
        line = line.strip()
        insertions[line[0:2]] = line[-1]
        for c in line:
            if c.isalpha():
                if c not in letters:
                    letters[c] = 0
    
    for i in range(40):
        tmp_pairs = defaultdict(int)
        for pair, count in pairs.items():
            tmp_pairs[pair[0]+insertions[pair]] += count
            tmp_pairs[insertions[pair]+pair[1]] += count
        pairs = tmp_pairs

    print(pairs)

    for p, c in pairs.items():
        for l in letters:
            if l in p:
                letters[l] += c
                if p == l+l:
                    letters[l] += c
    for l in letters:
        if letters[l] % 2:
            letters[l] += 1
        letters[l] //= 2
    
    print(letters)
    cnt = Counter(letters)
    most = cnt.most_common(1)[0][1]
    least = cnt.most_common()[-1][1]
    print(most-least)

@lru_cache(maxsize=0, typed=False)
def day15():
    file = open("aoc2021/15.in", "r")
    lines = file.readlines()
    file.close()

    for i, line in enumerate(lines):
        lines[i] = [int(c) for c in line.strip()]
    
    m = n = len(lines)

    risks = np.asarray(lines)

    print(risks)
    print(m, n)

    @lru_cache(maxsize=0, typed=False)
    def min_cost(x, y):
        if x < 0 or y < 0:
            return 900000000
        if x == 0 and y == 0:
            return 0
        return risks[y][x] + min(min_cost(x-1,y), min_cost(x,y-1))
    
    print(min_cost(m-1,n-1))



if __name__ == "__main__":
    day15()

    