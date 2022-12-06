# Day 6 - Part 1
with open('../inputs/day6.txt', 'r') as file:
    line = file.readline()
    for i in range(len(line)-3):
        code = list(line[i:i+4])
        if len(code) == len(set(code)):
            print(i+4)
            break

# Day 6 - Part 2
with open('../inputs/day6.txt', 'r') as file:
    line = file.readline()
    for i in range(len(line)-13):
        code = list(line[i:i+14])
        if len(code) == len(set(code)):
            print(i+14)
            break
