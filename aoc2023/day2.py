import re
def day2a():
    file2 = open('aoc2023/day2.input', 'r')
    Lines = file2.readlines()
    total = 0
    for line in Lines:
        print(line)
        game_number = int(re.findall(r'Game (\d+):', line)[0])
        reds = re.findall(r'((\d+) red)+', line)
        greens = re.findall(r'((\d+) green)+', line)
        blues = re.findall(r'((\d+) blue)+', line)
        # print(game_number, reds, greens, blues)
        max_red = max([int(r[1]) for r in reds])
        max_green = max([int(g[1]) for g in greens])
        max_blue = max([int(b[1]) for b in blues])
        print(game_number, max_red, max_green, max_blue)
        if max_red <= 12 and max_green <= 13 and max_blue <= 14:
            total += game_number
    print(total)
        
    file2.close()


def day2b():
    file2 = open('aoc2023/day2.input', 'r')
    Lines = file2.readlines()
    total = 0
    for line in Lines:
        print(line)
        game_number = int(re.findall(r'Game (\d+):', line)[0])
        reds = re.findall(r'((\d+) red)+', line)
        greens = re.findall(r'((\d+) green)+', line)
        blues = re.findall(r'((\d+) blue)+', line)
        # print(game_number, reds, greens, blues)
        max_red = max([int(r[1]) for r in reds])
        max_green = max([int(g[1]) for g in greens])
        max_blue = max([int(b[1]) for b in blues])
        print(game_number, max_red, max_green, max_blue)
        power = max_red * max_green * max_blue
        total += power
    print(total)

    file2.close()
    return 0