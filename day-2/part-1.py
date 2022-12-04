move_points = {
    'X': 1, # rock
    'Y': 2, # paper
    'Z': 3  # scissors
}

mapped_move = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

win_moves = [
    ('A', 'C'),
    ('C', 'B'),
    ('B', 'A')
]

def player_wins(player_move, opponent_move):
    return (player_move, opponent_move) in win_moves

def challenge_points(player_move, opponent_move):
    if player_wins(mapped_move[player_move], opponent_move):
        return 6
    elif mapped_move[player_move] == opponent_move:
        return 3
    return 0

total_points = 0

with open('input', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        opponent, player = line.split()

        round_points = move_points[player] + challenge_points(player, opponent)
        total_points += round_points
    
print(total_points)