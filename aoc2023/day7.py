import camelcards
from pprint import pprint

def day7a():
    file7 = open("aoc2023/day7.input", "r")
    Lines = file7.readlines()
    file7.close()
    hands = []
    for line in Lines:
        #print(line[0:5], line[6:])
        hands.append(camelcards.CamelCard(line[0:5], line[6:]))
    total = 0
    for position, h in enumerate(sorted(hands)):
        #print(h)
        total += (position + 1) * h.get_bid()
    print(total)
if __name__ == "__main__":
    day7a()