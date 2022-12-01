# Day 1 - Part 1
with open('../inputs/day1.txt', 'r') as file:
    max_sum = -1
    curr_sum = 0

    for line in file:
        line = line.strip()
        if line == '':
            max_sum = max(max_sum, curr_sum)
            curr_sum = 0
        else:
            value = int(line)
            curr_sum += value

    print(max_sum)

# Day 1 - Part 2
with open('../inputs/day1.txt', 'r') as file:
    values = []
    curr_sum = 0

    for line in file:
        line = line.strip()
        if line == '':
            values.append(curr_sum)
            curr_sum = 0
        else:
            value = int(line)
            curr_sum += value

    values.sort(reverse=True)
    print(sum(values[:3]))
