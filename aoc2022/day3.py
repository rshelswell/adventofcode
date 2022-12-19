def pt1():
    ret = 0
    with open('day3.input', 'r') as f:
        for l in f:
            a = l[:int(len(l) / 2)]
            b = l[int(len(l) / 2):]
            intersect = ord((set(a) & set(b)).pop())%64
            ret += intersect + 26 if intersect < 27 else intersect % 32
    return ret

print(pt1())

def pt2():
    ret = 0
    i = 0
    with open('day3.input', 'r') as f:
        a = list()
        b = list()
        c = list()
        for l in f:
            match i:
                case 2:
                    c=l[:-1]
                    i+=1
                case 1:
                    b=l[:-1]
                    i+=1
                case 0:
                    a=l[:-1]
                    i+=1
            print(a, b, c, i)
            if i == 3:
                intersect = ord((set(a) & set(b) & set(c)).pop()) % 64
                ret += intersect + 26 if intersect < 27 else intersect % 32
                i = 0
    return ret
print(pt2())