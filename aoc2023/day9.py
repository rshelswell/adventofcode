def get_differences(sequence, diffs=None):
    if diffs == None:
        diffs = [[u2-u for u, u2 in zip(sequence, sequence[1:])]]
    else:
        diffs.append([u2-u for u, u2 in zip(sequence, sequence[1:])])
    if all(i==0 for i in diffs[-1]):
        return diffs
    else:
        return get_differences(diffs[-1], diffs)



def day9():
    file9 = open("aoc2023/day9ex.input", "r")
    Lines = file9.readlines()
    file9.close()
    differences = []
    for line in Lines:
        seq = [int(i) for i in line.split()]
        next_n = len(seq) + 1
        differences.append(get_differences(seq))
        print(differences)

if __name__ == "__main__":
    day9()

