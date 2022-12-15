import re
def pt1():
    count = 0
    with open('day4.input', 'r') as f:
        for l in f:
            bounds = re.split(r'[,-]',l.strip())
            bounds = [int(x) for x in bounds]
            print(bounds)
            if (bounds[0] <= bounds[2] and bounds[1] >= bounds[3]) \
                or (bounds[2] <= bounds[0] and bounds[3] >= bounds[1]):
                count += 1
    return count

def pt2():
    count = 0
    with open('day4.input', 'r') as f:
        for l in f:
            bounds = re.split(r'[,-]',l.strip())
            bounds = [int(x) for x in bounds]
            # print(bounds)
            a = set(range(bounds[0],bounds[1]+1))
            b = set(range(bounds[2],bounds[3]+1))
            # print(a, b)
            if a & b:
                count += 1
    return count

print('part 1: ', pt1())
print('part 2: ', pt2())