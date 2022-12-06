import copy

initial_stacks = {
    1: ['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P'],
    2: ['M', 'Q', 'H'],
    3: ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L'],
    4: ['Z', 'T', 'F', 'Q', 'M', 'W', 'G'],
    5: ['M', 'T', 'H', 'P'],
    6: ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T'],
    7: ['M', 'N', 'B', 'F', 'V', 'R'],
    8: ['P', 'L', 'H', 'M', 'R', 'G', 'S'],
    9: ['P', 'D', 'B', 'C', 'N']
}


# Day 5 - Part 1
def move_crates(stacks, cnt, from_stack, to_stack):
    for i in range(cnt):
        crate = stacks[from_stack].pop()
        stacks[to_stack].append(crate)


with open('../inputs/day5.txt', 'r') as file:
    file = file.readlines()[10:]

    stacks = copy.deepcopy(initial_stacks)

    for line in file:
        line = line.strip()
        _, cnt, _, from_stack, _, to_stack = line.split(' ')
        cnt, from_stack, to_stack = int(cnt), int(from_stack), int(to_stack)
        move_crates(stacks, cnt, from_stack, to_stack)

    result = ''
    for stack in stacks:
        result += stacks[stack][-1]

    print(result)


# Day 5 - Part 2
def move_crates(stacks, cnt, from_stack, to_stack):
    crates = stacks[from_stack][-cnt:]
    stacks[from_stack] = stacks[from_stack][:-cnt]
    stacks[to_stack] += crates


with open('../inputs/day5.txt', 'r') as file:
    file = file.readlines()[10:]

    stacks = copy.deepcopy(initial_stacks)

    for line in file:
        line = line.strip()
        _, cnt, _, from_stack, _, to_stack = line.split(' ')
        cnt, from_stack, to_stack = int(cnt), int(from_stack), int(to_stack)
        move_crates(stacks, cnt, from_stack, to_stack)

    result = ''
    for stack in stacks:
        result += stacks[stack][-1]

    print(result)
