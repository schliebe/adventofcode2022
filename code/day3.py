# Day 3 - Part 1
with open('../inputs/day3.txt', 'r') as file:
    points = 0

    for line in file:
        line = line.strip()
        split_pos = len(line)//2
        comp_a, comp_b = line[:split_pos], line[split_pos:]
        for c in comp_a:
            if c in comp_b:
                char_num = ord(c)
                points += char_num - 96 if char_num > 90 else char_num - 38
                break

    print(points)

# Day 3 - Part 2
with open('../inputs/day3.txt', 'r') as file:
    points = 0
    group = []

    for line in file:
        line = line.strip()
        group.append(line)
        if len(group) == 3:
            for c in group[0]:
                if c in group[1] and c in group[2]:
                    char_num = ord(c)
                    points += char_num - 96 if char_num > 90 else char_num - 38
                    break
            group.clear()

    print(points)
