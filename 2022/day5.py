import re
def pt1():
    with open('day5.input', 'r') as f:
        initialise = True
        stacks = []
        line = 1
        for l in f:
            if initialise:
                if line == 1:
                    stacks = [[] for c in range(len(l)//4)]
                    line = 0
                if l[0] != '[':
                    initialise = False
                    continue
                for i in range(1,len(l),4):
                    if l[i] != ' ':
                        (stacks[i//4]).insert(0, l[i])
            elif len(l.strip()):
                # get the shuffling information
                instructions = [int(x) for x in re.findall(r'(\d+)+',l.strip())]
                # print(instructions)

                for j in range(instructions[0]):
                    stacks[instructions[2]-1].append(stacks[instructions[1]-1].pop())
   #            stacks[instructions[1] - 1] = stacks[instructions[1]-1][:0-instructions[0]]
                # print(stacks)
    ret = [s.pop() for s in stacks]
    return ''.join(ret)
def pt2():
    with open('day5.input', 'r') as f:
        initialise = True
        stacks = []
        line = 1
        for l in f:
            if initialise:
                if line == 1:
                    stacks = [[] for c in range(len(l) // 4)]
                    line = 0
                if l[0] != '[':
                    initialise = False
                    continue
                for i in range(1, len(l), 4):
                    if l[i] != ' ':
                        (stacks[i // 4]).insert(0, l[i])
            elif len(l.strip()):
                # get the shuffling information
                instructions = [int(x) for x in re.findall(r'(\d+)+', l.strip())]
                print(instructions)
                stacks[instructions[2] - 1] += stacks[instructions[1]-1][0-instructions[0]:]
                stacks[instructions[1] - 1] = stacks[instructions[1]-1][:0-instructions[0]]
                # print(stacks)
    ret = [s.pop() for s in stacks]
    return ''.join(ret)
    return stacks

# print('part 1: ', pt1())
print('part 2: ', pt2())