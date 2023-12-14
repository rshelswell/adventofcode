from pprint import pprint

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

def day9b():
    file9 = open("aoc2022/day9ex.input", "r")
    lines = file9.readlines()
    file9.close()
    tail_locations = set()
    tail_locations.add(tuple([0,0]))
    parts = [[0,0] for i in range(10)]
    pprint(parts)
    for line in lines:
        direction = line[0]
        repeats = int(line[2:].strip())
        print(direction, repeats)
        for r in range(repeats):
            if direction == "R":
                parts[0][0] += 1
            elif direction == "L":
                parts[0][0] -= 1
            elif direction == "U":
                parts[0][1] += 1
            elif direction == "D":
                parts[0][1] -= 1
            for p in range(9):
                if not is_adjacent(parts[p], parts[p+1]):
                    oldxy = [parts[p+1][0],parts[p+1]]
                    match direction:
                        case "R":
                            parts[p+1] = [parts[p][0]-1,parts[p][1]]
                        case "L":
                            parts[p+1] = [parts[p][0]+1,parts[p][1]]
                        case "U":
                            parts[p+1] = [parts[p][0],parts[p][1]-1]
                        case "D":
                            parts[p+1] = [parts[p][0],parts[p][1]+1]
                    delta_xy = [parts[p+1][0] - oldxy[0], parts[p+1][1] - oldxy[1]]
                    match delta_xy:
                        case [1,0]: #R
                            direction = "R"
                        case [-1,0]: #L
                            direction = "L"
                        case [0,1]: #U
                            direction = "U"
                        case [1,0]: #D
                            direction = "D"
                else:
                    break
            tail_locations.add((parts[-1][0],parts[-1][1]))
        print(parts)
        
            
    print(f"End position of head is {parts[0]}")
    print(f"End position of tail is {parts[-1]}")
    print(f"Tail visited {len(tail_locations)} places")

if __name__ == "__main__":
    day9b()