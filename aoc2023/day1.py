import re

def day1a():
    file1 = open('aoc2023/day1.input', 'r')
    Lines = file1.readlines()
    total = 0
    for line in Lines:
        digits = list(filter(lambda x: x.isdigit(), line))
        #print(f"Line{digits}: {line}")
        total += int(digits[0] + digits[-1])
    print(total)

def day1b():
    file1 = open('aoc2023/day1.input', 'r')
    Lines = file1.readlines()
    total = 0
    numbers = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0}
    for line in Lines:
        digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))', line)
        print(digits)
        if digits[0].isdigit():
            d1 = int(digits[0])
        else:
            d1 = numbers.get(digits[0])
        if digits[-1].isdigit():
            d2 = int(digits[-1])
        else:
            d2 = numbers.get(digits[-1])
        print(d1, d2)
        total += 10*d1+d2
    print(total)