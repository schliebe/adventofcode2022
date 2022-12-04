# Day 4 - Part 1
with open('../inputs/day4.txt', 'r') as file:
    cnt = 0

    for line in file:
        line = line.strip()
        a, b = line.split(',')
        a_from, a_to = a.split('-')
        b_from, b_to = b.split('-')
        a_from, a_to, b_from, b_to = int(a_from), int(a_to), int(b_from), int(b_to)
        if (b_from >= a_from and b_to <= a_to) or (a_from >= b_from and a_to <= b_to):
            cnt += 1

    print(cnt)

# Day 4 - Part 2
with open('../inputs/day4.txt', 'r') as file:
    cnt = 0

    for line in file:
        line = line.strip()
        a, b = line.split(',')
        a_from, a_to = a.split('-')
        b_from, b_to = b.split('-')
        a_from, a_to, b_from, b_to = int(a_from), int(a_to), int(b_from), int(b_to)
        if (b_from <= a_to and b_to >= a_from) or (a_from <= b_to and a_to >= b_from):
            cnt += 1

    print(cnt)
