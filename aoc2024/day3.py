import re

def day_3a():
    f = open("aoc2024/day3.input", "r")
    lines = f.readlines()
    f.close()
    s = 0
    for line in lines:
        x = re.findall("mul\((\d{1,3}),(\d{1,3})\)", line)
        s += sum([int(a[0])*int(a[1]) for a in x])
    print(s)

def day_3b():
    f = open("aoc2024/day3.input", "r")
    lines = f.readlines()
    f.close()
    s = 0
    do = True
    for line in lines:
        x = re.findall("(don't\(\)|do\(\)|mul\((\d{1,3}),(\d{1,3})\))", line)
        print(x)
        for a in x:
            if a[0] == "do()":
                do = True
            elif a[0] == "don't()":
                do = False
            elif do:
                s += int(a[1])*int(a[2])
    print(s)

