def is_touching(head, tail):
    h_x, h_y = head
    t_x, t_y = tail

    return abs(h_x - t_x) <= 1 and abs(h_y - t_y) <= 1


# Day 9 - Part 1
"""
with open('../inputs/day9.txt', 'r') as file:
    head_x, head_y, tail_x, tail_y = 0, 0, 0, 0
    visited = [(tail_x, tail_y)]

    for line in file:
        line = line.strip()
        direction, distance = line.split(' ')
        distance = int(distance)

        for i in range(distance):
            if direction == 'R':
                new_x, new_y = head_x + 1, head_y
            elif direction == 'L':
                new_x, new_y = head_x - 1, head_y
            elif direction == 'U':
                new_x, new_y = head_x, head_y + 1
            elif direction == 'D':
                new_x, new_y = head_x, head_y - 1
            else:
                # Should never go here
                new_x, new_y = head_x, head_y

            if not is_touching((new_x, new_y), (tail_x, tail_y)):
                new_pos = (head_x, head_y)
                if new_pos not in visited:
                    visited.append(new_pos)
                tail_x, tail_y = head_x, head_y
            head_x, head_y = new_x, new_y

    print(len(visited))
"""


# Day 9 - Part 2
def normalize(value):
    # normalize value between -1 and 1
    if value >= 1:
        return 1
    elif value <= -1:
        return -1
    else:
        return value


class Node:
    id = None
    x = 0
    y = 0
    last_pos = (0, 0)
    parent = None
    child = None
    visited = []

    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.visited = {(x, y)}

    def set_child(self, child):
        self.child = child
        child.set_parent(self)
        return child

    def set_parent(self, parent):
        self.parent = parent

    def is_touching(self, node):
        return abs(self.x - node.x) <= 1 and abs(self.y - node.y) <= 1

    def move_to(self, x, y):
        self.x = x
        self.y = y
        if self.child:
            self.child.follow_parent()
        else:
            if (x, y) not in self.visited:
                self.visited.add((x, y))

    # only used by head
    def move_in_direction(self, direction):
        last_x, last_y = self.x, self.y
        if direction == 'R':
            self.move_to(self.x + 1, self.y)
        elif direction == 'L':
            self.move_to(self.x - 1, self.y)
        elif direction == 'U':
            self.move_to(self.x, self.y + 1)
        elif direction == 'D':
            self.move_to(self.x, self.y - 1)

    def follow_parent(self):
        if not self.is_touching(self.parent):
            diff_x = normalize(self.parent.x - self.x)
            diff_y = normalize(self.parent.y - self.y)
            if diff_x != 0 or diff_y != 0:
                self.move_to(self.x + diff_x, self.y + diff_y)


def print_positions(node):
    while node:
        print(node. id, (node.x, node.y))
        node = node.child


with open('../inputs/day9.txt', 'r') as file:
    head = Node('H', 0, 0)
    node = head
    for i in range(1, 10):
        node = node.set_child(Node(i, 0, 0))
    tail = node

    for line in file:
        line = line.strip()
        direction, distance = line.split(' ')
        distance = int(distance)

        for i in range(distance):
            head.move_in_direction(direction)
            #print('--------')
            #print_positions(head)

    print(len(tail.visited))
    print(tail.visited)
