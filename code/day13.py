import json
from functools import cmp_to_key


def right_order(left, right):
    if isinstance(left, int):
        if isinstance(right, int):
            # Both values are int
            if left == right:
                return 0
            else:
                return right - left
        else:
            # Convert left to list
            left = [left]
    else:
        if isinstance(right, int):
            # Convert right to list
            right = [right]

    # Both values are lists
    left_len, right_len = len(left), len(right)
    for i in range(min(left_len, right_len)):
        res = right_order(left[i], right[i])
        if res != 0:
            return res
    if left_len == right_len:
        return 0
    else:
        return right_len - left_len


with open('../inputs/day13.txt', 'r') as file:
    input_list = []

    left = None
    right = None
    for line in file:
        if left is None:
            left = json.loads(line.strip())
        elif right is None:
            right = json.loads(line.strip())
            input_list.append((left, right))
        else:
            # Skip empty line
            left = right = None

    result = 0
    run = 1

    for line in input_list:
        left, right = line
        if right_order(left, right) > 0:
            result += run
        run += 1

    print(result)

    sep1, sep2 = [[2]], [[6]]
    new_input_list = [sep1, sep2]
    for elem in input_list:
        left, right = elem
        new_input_list.append(left)
        new_input_list.append(right)
    new_input_list.sort(key=cmp_to_key(right_order), reverse=True)
    print((new_input_list.index(sep1) + 1) * (new_input_list.index(sep2) + 1))
