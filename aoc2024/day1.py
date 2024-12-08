from collections import Counter

def day_1a():
    f = open("aoc2024/day1.input", "r")
    lines = f.readlines()
    f.close()
    loc_IDa = []
    loc_IDb = []
    for line in lines:
        loc_IDa.append(int(line.split()[0]))
        loc_IDb.append(int(line.split()[1]))
    loc_IDa = sorted(loc_IDa)
    loc_IDb = sorted(loc_IDb)
    diffs = []
    for l1, l2 in zip(loc_IDa, loc_IDb):
        diffs.append(abs(l1-l2))
    print("differences:", sum(diffs))

    id_count = Counter(loc_IDb)
    sum_products = 0
    for loc_ID in loc_IDa:
        sum_products += loc_ID * id_count[loc_ID]
    print("Sum of products:", sum_products)
