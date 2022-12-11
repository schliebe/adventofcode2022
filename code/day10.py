# Day 10 - Part 1
with open('../inputs/day10.txt', 'r') as file:
    cycle = 1
    x = 1

    result = 0

    cycle_list = [20, 60, 100, 140, 180, 220]

    def check_cycle_list():
        global result, cycle, cycle_list
        if cycle in cycle_list:
            result += cycle * x

    for line in file:
        line = line.strip()
        if line.startswith('noop'):
            check_cycle_list()
            cycle += 1
        elif line.startswith('addx'):
            command, param = line.split(' ')
            param = int(param)
            check_cycle_list()
            cycle += 1
            check_cycle_list()
            cycle += 1
            x += param

    print(result)

# Day 10 - Part 2
with open('../inputs/day10.txt', 'r') as file:
    cycle = 0
    x = 1

    result = ''

    def draw_pixel():
        global cycle, x, result
        if cycle % 40 in range(x - 1, x + 2):
            result += '#'
        else:
            result += '.'

    for line in file:
        line = line.strip()
        if line.startswith('noop'):
            draw_pixel()
            cycle += 1
        elif line.startswith('addx'):
            command, param = line.split(' ')
            param = int(param)
            draw_pixel()
            cycle += 1
            draw_pixel()
            cycle += 1
            x += param

    for i in range(6):
        print(result[40*i:40*(i+1)])
