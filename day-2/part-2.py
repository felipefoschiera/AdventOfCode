move_points = {
    'A': 1, # rock
    'B': 2, # paper
    'C': 3  # scissors
}

lose_move = {
    'A': 'C',
    'C': 'B',
    'B': 'A'
}   

win_moves = [
    ('A', 'C'),
    ('C', 'B'),
    ('B', 'A')
]

win_move = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

def find_best_move(opponent_move, result):
    if result == 'Y':
        return opponent_move
    if result == 'X':
        return lose_move[opponent_move]
    return win_move[opponent_move]

def player_wins(player_move, opponent_move):
    return (player_move, opponent_move) in win_moves

def challenge_points(player_move, opponent_move):
    if player_wins(player_move, opponent_move):
        return 6
    elif player_move == opponent_move:
        return 3
    return 0

total_points = 0

with open('input', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        opponent, result = line.split()

        player_move = find_best_move(opponent, result)
        round_points = move_points[player_move] + challenge_points(player_move, opponent)
        
        total_points += round_points
    
print(total_points)