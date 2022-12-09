def read_file(file):
    lines = []
    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            lines.append(line)
    return lines


def build_grid(lines):
    grid = []
    for line in lines:
        chars = list(map(int, list(line)))
        grid.append(chars)
    return grid


def count_up(grid, row, col):
    count = 0
    for k in range(row-1, -1, -1):
        count += 1
        if grid[k][col] >= grid[row][col]:
            break
    return count


def count_down(grid, row, col):
    rows = len(grid)
    count = 0
    for k in range(row+1, rows):
        count += 1
        if grid[k][col] >= grid[row][col]:
            break
    return count


def count_left(grid, row, col):
    count = 0
    for k in range(col-1, -1, -1):
        count += 1
        if grid[row][k] >= grid[row][col]:
            break
    return count


def count_right(grid, row, col):
    cols = len(grid[0])
    count = 0
    for k in range(col+1, cols):
        count += 1
        if grid[row][k] >= grid[row][col]:
            break
    return count


def find_best_scenic_view(grid):
    rows, cols = len(grid), len(grid[0])
    best_scenic = 0

    for row in range(1, rows-1):
        for col in range(1, cols-1):
            current_cell = grid[row][col]

            scenic_view = 1
            scenic_view *= count_up(grid, row, col)
            scenic_view *= count_down(grid, row, col)
            scenic_view *= count_left(grid, row, col)
            scenic_view *= count_right(grid, row, col)

            best_scenic = max(best_scenic, scenic_view)
    return best_scenic


lines = read_file('input')
grid = build_grid(lines)

best_scenic = find_best_scenic_view(grid)
print(best_scenic)
