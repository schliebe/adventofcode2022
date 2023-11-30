# Day 14 - Part 1
def left(pos):
    x, y = pos
    return x - 1, y


def right(pos):
    x, y = pos
    return x + 1, y


def up(pos):
    x, y = pos
    return x, y - 1


def down(pos):
    x, y = pos
    return x, y + 1


class Grid:
    grid = {}
    min_x, max_x, min_y, max_y = None, None, None, None

    def __init__(self, default):
        self.default = default

    def get(self, pos):
        x, y = pos
        if x in self.grid:
            if y in self.grid[x]:
                return self.grid[x][y]

        return self.default

    def set(self, pos, value):
        x, y = pos
        if x in self.grid:
            self.grid[x][y] = value
        else:
            self.grid[x] = {
                y: value
            }
        self.update_min_max(x, y)

    def update_min_max(self, x, y):
        if self.min_x:
            self.min_x = min(self.min_x, x)
        else:
            self.min_x = x

        if self.max_x:
            self.max_x = max(self.max_x, x)
        else:
            self.max_x = x

        if self.min_y:
            self.min_y = min(self.min_y, y)
        else:
            self.min_y = y

        if self.max_y:
            self.max_y = max(self.max_y, y)
        else:
            self.max_y = y

    def set_from_to(self, from_pos, to_pos, value):
        x_from, y_from = from_pos
        x_to, y_to = to_pos
        if x_from == x_to:
            for y in range(min(y_from, y_to), max(y_from, y_to) + 1):
                self.set((x_from, y), value)
        else:
            for x in range(min(x_from, x_to), max(x_from, x_to) + 1):
                self.set((x, y_from), value)

    def drop_sand(self, sand_pos):
        if self.get(sand_pos) != '.':
            # Source is blocked
            return True
        while True:
            below = self.get(down(sand_pos))
            if below == '.':
                # Keep falling
                sand_pos = down(sand_pos)
            elif below == '~':
                # Falling to the void
                return True
            else:
                # Hit the ground
                # Look down left
                down_left = self.get(left(down(sand_pos)))
                if down_left == '~':
                    return True
                elif down_left == '.':
                    sand_pos = left(down(sand_pos))
                else:
                    # Look down right
                    down_right = self.get(right(down(sand_pos)))
                    if down_right == '~':
                        return True
                    elif down_right == '.':
                        sand_pos = right(down(sand_pos))
                    else:
                        self.set(sand_pos, 'O')
                        return False


with open('../inputs/day14.txt', 'r') as file:
    grid = Grid('.')

    # Create grid
    for line in file:
        rocks = []
        line.strip()
        point_list = line.split(' -> ')
        for point in point_list:
            x, y = point.split(',')
            x, y = int(x), int(y)
            rocks.append((x, y))

        for i in range(len(rocks) - 1):
            grid.set_from_to(rocks[i], rocks[i + 1], '#')

    # Set line of ~ to indicate void
    min_x, max_x, max_y = grid.min_x, grid.max_x, grid.max_y
    grid.set_from_to((min_x - 1, max_y + 1), (max_x + 1, max_y + 1), '~')

    sand_cnt = 0
    res = False
    while not res:
        sand_cnt += 1
        res = grid.drop_sand((500, 0))

    print(sand_cnt - 1)

# Day 14 - Part 2
with open('../inputs/day14.txt', 'r') as file:
    grid = Grid('.')

    # Create grid
    for line in file:
        rocks = []
        line.strip()
        point_list = line.split(' -> ')
        for point in point_list:
            x, y = point.split(',')
            x, y = int(x), int(y)
            rocks.append((x, y))

        for i in range(len(rocks) - 1):
            grid.set_from_to(rocks[i], rocks[i + 1], '#')

    # Set ground
    min_x, max_x, max_y = grid.min_x, grid.max_x, grid.max_y
    grid.set_from_to((min_x - 200, max_y + 2), (max_x + 200, max_y + 2), '#')

    sand_cnt = 0
    res = False
    while not res:
        sand_cnt += 1
        res = grid.drop_sand((500, 0))

    print(sand_cnt - 1)
