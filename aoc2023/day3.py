import re
from pprint import pprint
from collections import Counter

def day3a():
    file3 = open('aoc2023/day3.input', 'r')
    line_num = 0
    sym_locations = dict()
    num_locations = dict()
    Lines = file3.readlines()
    total = 0
    file3.close()
    for line in Lines:
        sym_matches = re.finditer(r'([^.\d\n])', line)
        sym_locations.update({line_num: list((s.start() for s in sym_matches))})
          
        num_matched = re.finditer(r'(\d+)', line)
        num_locations.update({line_num: list((n.group(), n.span()[0]) for n in num_matched)})
        line_num += 1
    #print(sym_locations)
    #print(num_locations)
    for line, part_nums in num_locations.items():
        llen = len(Lines[line])
        for n, p in part_nums:
            nl = len(n)
            checkpos = [i for i in range(max(0, p - 1), min(p + nl + 1, llen))]
#            print(nl, checkpos)
            if any(map(lambda v: v in sym_locations[max(0,line-1)], checkpos)) or any(map(lambda v: v in sym_locations[min(line_num-1,line+1)], checkpos)) or any(map(lambda v: v in sym_locations[line], checkpos)):
               total += int(n)
            #print(f'line = {line} and total = {total}')
    #print(sym_locations)
    print(total)

def day3b():
    file3 = open('aoc2023/day3.input', 'r')
    line_num = 0
    sym_locations = dict()
    Lines = file3.readlines()
    file3.close()
    possible_gear_locations = dict()
    total = 0
    for line in Lines:
        sym_matches = re.finditer(r'([*])', line)
        sym_locations.update({line_num: list((s.start() for s in sym_matches))})
        num_matched = re.finditer(r'(\d+)', line)
        for n in num_matched:
            num_start = n.span()[0]
            num_end = num_start + len(n.group())
            num = int(n.group())
            #for i in range(max(0, num_start-1), min(num_end+1, len(line))):
            if line_num > 0:
                if line_num-1 not in possible_gear_locations:
                    possible_gear_locations.update({line_num-1: [(i, num) for i in range(max(0, num_start-1), min(num_end+1, len(line)))]})
                else:
                    possible_gear_locations[line_num-1].extend([(i, num) for i in range(max(0, num_start-1), min(num_end+1, len(line)))])
            if line_num+1 not in possible_gear_locations:
                possible_gear_locations.update({line_num+1: [(i, num) for i in range(max(0, num_start-1), min(num_end+1, len(line)))]})
            else:
                possible_gear_locations[line_num+1].extend([(i, num) for i in range(max(0, num_start-1), min(num_end+1, len(line)))])
            if num_start > 0:
                if line_num not in possible_gear_locations:
                    possible_gear_locations.update({line_num: [(num_start-1, num)]})
                else:
                    possible_gear_locations[line_num].extend([(num_start-1, num)])
            if num_end < len(line):
                if line_num not in possible_gear_locations:
                    possible_gear_locations.update({line_num: [(num_end, num)]})
                else:
                    possible_gear_locations[line_num].extend([(num_end, num)])
        line_num += 1

    #pprint(possible_gear_locations)
    
    for l, p in sym_locations.items():
        if len(p) > 0:
            for pos in p:
                print(l, p)
                c = Counter(elem[0] for elem in possible_gear_locations[l])
                if c[pos] == 2:
                    gears = [elem[1] for elem in possible_gear_locations[l] if elem[0] == pos]
                    total += gears[0] * gears[1]
    print(total)
#    print(sym_locations)
#    print(total)
