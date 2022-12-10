def read_file(file):
    play_moves = []
    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            direction, moves = line.split()
            play_moves.append((direction, int(moves)))
    return play_moves

play_moves = read_file('input')

t_visited = [(0, 0)]
t_pos = (0, 0)
h_pos = (0, 0)

'''
4
3
2
1
012345
'''

def are_touching(h_pos, t_pos):
    are_overlapping = h_pos == t_pos
    y_diff = abs(h_pos[0] - t_pos[0])
    x_diff = abs(h_pos[1] - t_pos[1])
    are_side = y_diff + x_diff == 1
    are_diagonal = y_diff == 1 and x_diff == 1
    return (are_overlapping or are_side or are_diagonal)

def two_in_direction(h_pos, t_pos):
    y_diff = abs(h_pos[0] - t_pos[0])
    x_diff = abs(h_pos[1] - t_pos[1])
    return (y_diff == 2 and x_diff == 0) or (x_diff == 2 and y_diff == 0)

def move_to_direction(h_pos, t_pos):
    # if h_pos is two to the right
    if h_pos[1] - t_pos[1] == 2 and h_pos[0] == t_pos[0]:
        return (t_pos[0], t_pos[1] + 1)
    # if h_pos is two to the left
    if t_pos[1] - h_pos[1] == 2 and h_pos[0] == t_pos[0]:
        return (t_pos[0], t_pos[1] - 1)
    # if h_pos is two up
    if h_pos[0] - t_pos[0] == 2 and h_pos[1] == t_pos[1]:
        return (t_pos[0] + 1, t_pos[1])
    # if h_pos is two down
    if t_pos[0] - h_pos[0] == 2 and h_pos[1] == t_pos[1]:
        return (t_pos[0] - 1, t_pos[1])
    
    # h (2, 4), t (0, 3)

    # 4     h   
    # 3         t 
    # 2          
    # 1         
    # 0       
    # X 0 1 2 3 4 5
def move_diagonal(h_pos, t_pos):
    y_diff = h_pos[0] - t_pos[0]
    x_diff = h_pos[1] - t_pos[1]
    
    if (y_diff == 2 and x_diff == 1) or (y_diff == 1 and x_diff == 2):
        return (t_pos[0] + 1, t_pos[1] + 1)
    if (y_diff == 2 and x_diff == -1) or (y_diff == 1 and x_diff == -2):
        return (t_pos[0] + 1, t_pos[1] - 1)
    if (y_diff == -2 and x_diff == 1) or (y_diff == -1 and x_diff == 2):
        return (t_pos[0] - 1, t_pos[1] + 1)
    if (y_diff == -2 and x_diff == -1) or (y_diff == -1 and x_diff == -2):
        return (t_pos[0] - 1, t_pos[1] - 1)
    
for direction, moves in play_moves:
    for i in range(moves):
        starting_y, starting_x = h_pos
        if direction == 'R':
            h_pos = (starting_y, starting_x + 1)
        elif direction == 'U':
            h_pos = (starting_y + 1, starting_x)
        elif direction ==  'L':
            h_pos = (starting_y, starting_x - 1)
        elif direction == 'D':
            h_pos = (starting_y - 1, starting_x)
        
        if not are_touching(h_pos, t_pos):
            if two_in_direction(h_pos, t_pos):
                t_pos = move_to_direction(h_pos, t_pos)
            else:
                t_pos = move_diagonal(h_pos, t_pos)
        
        t_visited.append(t_pos)

t_visited = set(t_visited)
print(len(t_visited))