# Day 2 - Part 1
pts_played = {
    'X': 1,  # Rock
    'Y': 2,  # Paper
    'Z': 3,  # Scissors
}

pts_result = {
    'A': {  # Rock
        'X': 3,  # Draw
        'Y': 6,  # Win
        'Z': 0,  # Loss
    },
    'B': {  # Paper
        'X': 0,
        'Y': 3,
        'Z': 6,
    },
    'C': {  # Scissors
        'X': 6,
        'Y': 0,
        'Z': 3,
    },
}

with open('../inputs/day2.txt', 'r') as file:
    points = 0

    for line in file:
        line = line.strip()
        opp, me = line.split(' ')
        points += pts_played[me]
        points += pts_result[opp][me]

    print(points)

# Day 2 - Part 2
pts_played = {
    'A': 1,  # Rock
    'B': 2,  # Paper
    'C': 3,  # Scissors
}

pts_result = {
    'X': 0,  # Loss
    'Y': 3,  # Draw
    'Z': 6,  # Win
}

choose_me = {
    'A': {  # Rock
        'X': 'C',  # Loss
        'Y': 'A',  # Draw
        'Z': 'B',  # Win
    },
    'B': {  # Paper
        'X': 'A',
        'Y': 'B',
        'Z': 'C',
    },
    'C': {  # Scissors
        'X': 'B',
        'Y': 'C',
        'Z': 'A',
    },
}

with open('../inputs/day2.txt', 'r') as file:
    points = 0

    for line in file:
        line = line.strip()
        opp, res = line.split(' ')
        me = choose_me[opp][res]
        points += pts_played[me]
        points += pts_result[res]

    print(points)
