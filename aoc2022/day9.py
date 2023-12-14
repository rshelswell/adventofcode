def is_adjacent(pair1, pair2):
    return abs(pair1[0]-pair2[0]) < 2 and abs(pair1[1]-pair2[1]) < 2


def day9a():
    file9 = open("aoc2022/day9.input", "r")
    lines = file9.readlines()
    file9.close()
    tail_locations = set()
    tail_locations.add(tuple([0,0]))
    head = [0,0]
    last_head = [0,0]
    tail = [0,0]
    last_tail = [0,0]
    for line in lines:
        direction = line[0]
        repeats = int(line[2:].strip())
        print(direction, repeats)
        for r in range(repeats):
            if direction == "R":
                head[0] += 1
            elif direction == "L":
                head[0] -= 1
            elif direction == "U":
                head[1] += 1
            elif direction == "D":
                head[1] -= 1
            if not is_adjacent(head, tail):
                match direction:
                    case "R":
                        tail = [head[0]-1,head[1]]
                    case "L":
                        tail = [head[0]+1,head[1]]
                    case "U":
                        tail = [head[0],head[1]-1]
                    case "D":
                        tail = [head[0],head[1]+1]
            tail_locations.add((tail[0],tail[1]))
        print(head)
        print(tail, "\n")
            
    print(f"End position of head is {head}")
    print(f"End position of tail is {tail}")
    print(f"Tail visited {len(tail_locations)} places")

if __name__ == "__main__":
    day9a()