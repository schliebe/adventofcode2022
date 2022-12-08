# Day 8 - Part 1
with open('../inputs/day8.txt', 'r') as file:
    grid = []
    res_grid = []
    result = 0

    for line in file:
        line = line.strip()
        row = [int(c) for c in list(line)]
        grid.append(row)
        res_grid.append([False] * len(row))

    # Run from left to right
    for y in range(len(grid)):
        max_left = -1
        max_right = -1
        for x in range(len(grid[y])):
            # Run from the left
            val = grid[y][x]
            if val > max_left:
                max_left = val
                if res_grid[y][x] is not True:
                    res_grid[y][x] = True
                    result += 1

            # Run from the right
            val = grid[y][-x-1]
            if val > max_right:
                max_right = val
                if res_grid[y][-x-1] is not True:
                    res_grid[y][-x-1] = True
                    result += 1

    # Run from top to bottom
    for x in range(len(grid[0])):
        max_top = -1
        max_bottom = -1
        for y in range(len(grid)):
            # Run from the top
            val = grid[y][x]
            if val > max_top:
                max_top = val
                if res_grid[y][x] is not True:
                    res_grid[y][x] = True
                    result += 1

            # Run from the bottom
            val = grid[-y-1][x]
            if val > max_bottom:
                max_bottom = val
                if res_grid[-y-1][x] is not True:
                    res_grid[-y-1][x] = True
                    result += 1

    print(result)

# Day 8 - Part 2
with open('../inputs/day8.txt', 'r') as file:
    grid = []
    res_grid = []
    max_score = -1

    for line in file:
        line = line.strip()
        row = [int(c) for c in list(line)]
        grid.append(row)
        res_grid.append([0] * len(row))

    y_size, x_size = len(grid), len(grid[0])
    for y in range(y_size):
        for x in range(x_size):
            score_left, score_right, score_top, score_bottom = 0, 0, 0, 0
            height = grid[y][x]

            # Look to the left
            for i in range(x):
                score_left += 1
                if grid[y][x-i-1] >= height:
                    break

            # Look to the right
            for i in range(x_size - x - 1):
                score_right += 1
                if grid[y][x + i + 1] >= height:
                    break

            # Look to the top
            for i in range(y):
                score_top += 1
                if grid[y - i - 1][x] >= height:
                    break

            # Look to the bottom
            for i in range(y_size - y - 1):
                score_bottom += 1
                if grid[y + i + 1][x] >= height:
                    break

            # Compute scenic_score
            score = score_left * score_right * score_top * score_bottom
            res_grid[y][x] = score
            if score > max_score:
                max_score = score

    print(max_score)
