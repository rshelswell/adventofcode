from itertools import pairwise, combinations
from collections import Counter

def report_safety(report):
    if report == sorted(report) or report == sorted(report, reverse=True):
        #all increasing or decreasing
        diffs = [abs(a-b) for a, b in pairwise(report)]
        #print(diffs)
        return all(1 <= diff <= 3 for diff in diffs)

def day_2a():
    f = open("aoc2024/day2.input")
    lines = f.readlines()
    f.close()
    reports = [[int(x) for x in l.split()] for l in lines]
    safety = []
    #print(reports)
    for report in reports:
        safety.append(report_safety(report))
    #print(safety)
    c = Counter(safety)
    print("Safe reports:", c[True])

def day_2b():
    f = open("aoc2024/day2.input")
    lines = f.readlines()
    f.close()
    reports = [[int(x) for x in l.split()] for l in lines]
    safety = []
    #print(reports)
    for report in reports:
        if report_safety(report):
            safety.append(True)
        else:
            sublists = list(combinations(report, len(report)-1))
            print("sublists:", sublists)
            subsafety = False
            for sublist in sublists:
                if report_safety(list(sublist)):
                    subsafety = True
            safety.append(subsafety) 
    #print(safety)
    c = Counter(safety)
    print("Safe reports:", c[True])