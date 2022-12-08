class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def get_sum_under_threshold(self, threshold):
        return 0

    def get_dir_size_list(self):
        return []


class Directory(File):
    def __init__(self, name, parent):
        File.__init__(self, name, 0)
        self.childs = []
        self.parent = parent

    def add(self, add):
        self.childs.append(add)

    def get_dir(self, name):
        if name == '..':
            return self.parent
        else:
            for c in self.childs:
                if c.name == name and isinstance(c, Directory):
                    return c

    def get_size(self):
        sum = 0
        for c in self.childs:
            sum += c.get_size()
        return sum

    def get_sum_under_threshold(self, threshold):
        sum = 0
        for c in self.childs:
            sum += c.get_sum_under_threshold(threshold)

        if self.get_size() <= threshold:
            sum += self.get_size()

        return sum

    def get_dir_size_list(self):
        dir_list = []
        for c in self.childs:
            dir_list += c.get_dir_size_list()
        dir_list.append((self.name, self.get_size()))
        return dir_list


# Day 7 - Part 1
with open('../inputs/day7.txt', 'r') as file:
    root = Directory('root', None)
    root.add(Directory('/', root))
    curr_dir = root

    for line in file:
        line = line.strip()
        v1, v2 = line.split(' ', 1)
        if v1 == '$':
            if v2.startswith('cd'):
                _, new_dir = v2.split(' ')
                curr_dir = curr_dir.get_dir(new_dir)
        else:
            if v1 == 'dir':
                curr_dir.add(Directory(v2, curr_dir))
            else:
                curr_dir.add(File(v2, int(v1)))

print(root.get_sum_under_threshold(100000))

# Day 7 - Part 2
with open('../inputs/day7.txt', 'r') as file:
    root = Directory('root', None)
    root.add(Directory('/', root))
    curr_dir = root

    for line in file:
        line = line.strip()
        v1, v2 = line.split(' ', 1)
        if v1 == '$':
            if v2.startswith('cd'):
                _, new_dir = v2.split(' ')
                curr_dir = curr_dir.get_dir(new_dir)
        else:
            if v1 == 'dir':
                curr_dir.add(Directory(v2, curr_dir))
            else:
                curr_dir.add(File(v2, int(v1)))

dir_size_list = sorted(root.get_dir_size_list(), key=lambda tup: tup[1])

space_needed = root.get_size() - (70000000 - 30000000)

for d in dir_size_list:
    if d[1] > space_needed:
        print(d[1])
        break
