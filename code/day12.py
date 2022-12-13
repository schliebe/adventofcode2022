# Day 12 - Part 1
class Space:
    def __init__(self, pos, value, dist=None, direction=None):
        self.pos = pos
        self.value = value
        self.dist = dist
        self.direction = direction
        self.done = False

    def __repr__(self):
        return chr(self.value + 96)


with open('../inputs/day12.txt', 'r') as file:
    area_map = []
    start = None
    end = None

    # Build the area map
    y = 0
    for line in file:
        line.strip()
        row = list(line)
        map_row = []
        x = 0
        for r in row:
            if r == 'S':
                space = Space((x, y), 1)
                start = space
            elif r == 'E':
                space = Space((x, y), 26, 0)
                end = space
            else:
                value = ord(r) - 96
                space = Space((x, y), value)
            map_row.append(space)
            x += 1
        area_map.append(map_row)
        y += 1

    y_max, x_max = len(area_map), len(area_map[0])

    todo_list = [end]
    while len(todo_list) > 0:
        new_todo = []
        for space in todo_list:
            x, y = space.pos
            neighbors = []
            if x != 0:
                left = area_map[y][x - 1]
                if not left.done and left.value >= space.value - 1:
                    left.dist = space.dist + 1
                    left.direction = 'R'
                    left.done = True
                    new_todo.append(left)
            if x != x_max - 1:
                right = area_map[y][x + 1]
                if not right.done and right.value >= space.value - 1:
                    right.dist = space.dist + 1
                    right.direction = 'L'
                    right.done = True
                    new_todo.append(right)
            if y != 0:
                top = area_map[y - 1][x]
                if not top.done and top.value >= space.value - 1:
                    top.dist = space.dist + 1
                    top.direction = 'D'
                    top.done = True
                    new_todo.append(top)
            if y != y_max - 1:
                bottom = area_map[y + 1][x]
                if not bottom.done and bottom.value >= space.value - 1:
                    bottom.dist = space.dist + 1
                    bottom.direction = 'U'
                    bottom.done = True
                    new_todo.append(bottom)

        todo_list = new_todo

    print(start.dist)

# Day 12 - Part 2
min_dist = 10000
for y in range(len(area_map)):
    for x in range(len(area_map[y])):
        space = area_map[y][x]
        if space.done and space.value == 1:
            min_dist = min(min_dist, space.dist)

print(min_dist)
