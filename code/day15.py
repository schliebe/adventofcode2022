# Day 15 - Part 1
def calc_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)


with open('../inputs/day15.txt', 'r') as file:
    interval = []
    for line in file:
        # Input looks like:
        # Sensor at x=220580, y=684270: closest beacon is at x=436611, y=263737
        line = (line.replace('Sensor at x=', '')
                .replace(': closest beacon is at x=', ', ')
                .replace('y=', ''))
        s_x, s_y, b_x, b_y = line.split(', ')
        s_x, s_y, b_x, b_y = int(s_x), int(s_y), int(b_x), int(b_y)

        distance = calc_distance((s_x, s_y), (b_x, b_y))
        y_dist = abs(s_y - b_y)
        rest_dist = distance - y_dist

        if rest_dist > 0:
            interval.append((s_x - rest_dist, s_x + rest_dist))

    interval.sort(key=lambda x: x[0])
    final = []
    curr_interval = interval.pop(0)
    while len(interval) > 0:
        next = interval.pop(0)
        if curr_interval[1] >= next[0]:
            curr_interval = (curr_interval[0], max(curr_interval[1], next[1]))
        else:
            final.append(curr_interval)
            curr_interval = next
    final.append(curr_interval)

    res = 0
    for i in final:
        res += (i[1] - i[0])

    print(res)

# Day 15 - Part 2
