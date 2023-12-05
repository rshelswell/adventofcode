import re
from pprint import pprint


def day4a():
    file4 = open(r'aoc2023/day4.input', 'r')
    Lines = file4.readlines()
    file4.close()
    total = 0
    for line in Lines:
        nums = line.strip().split(":")[1].split("|")
        wins = list(map(int, nums[0].strip().split()))
        mine = list(map(int, nums[1].strip().split()))
        intersection = sum(1 for x in mine if x in wins)
        print(intersection)
        if intersection == 0:
            continue
        else:
            total += 2**(intersection -1)
    print(total)

def day4b():
    file4 = open(r'aoc2023/day4.input', 'r')
    Lines = file4.readlines()
    file4.close()
    games = dict()
    scoring = dict()
    for line in Lines:
        game_num = int(re.findall(r'(\d+):', line)[0])
        #print('game', game_num)
        games.update({game_num: 1})
        nums = line.strip().split(":")[1].split("|")
        wins = list(map(int, nums[0].strip().split()))
        mine = list(map(int, nums[1].strip().split()))
        intersection = sum(1 for x in mine if x in wins)
        #print(intersection)
        scoring.update({game_num: intersection})
    # pprint(games)
    # pprint(scoring)
    for game, cards in games.items():
        if game % 20 == 0:
            print(f"Game: {game}")
        if scoring[game] == 0:
            continue
        else:
            for w in range(1, scoring[game] + 1):
                if game+w in games:
                    games[game + w] = games[game + w] + games[game]
    print(f"cards: {sum(games.values())}")
    #pprint(games)
    #pprint(scoring)
    