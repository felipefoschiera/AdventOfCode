lines = []

with open('input', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        lines.append(line)


grid = []
for line in lines:
    chars = list(map(int, list(line)))
    grid.append(chars)


rows = len(grid)
cols = len(grid[0])

visible = (rows * 2) + (cols * 2) - 4

for row in range(1, rows-1):
    for col in range(1, cols-1):
        block_count = 0
        for k in range(0, row):
            if grid[k][col] >= grid[row][col]:
                block_count += 1
                break
        
        for k in range(row+1, rows):
            if grid[k][col] >= grid[row][col]:
                block_count += 1
                break

        for k in range(0, col):
            if grid[row][k] >= grid[row][col]:
                block_count += 1
                break


        for k in range(col+1, cols):
            if grid[row][k] >= grid[row][col]:
                block_count += 1
                break
            
        if block_count < 4:
            visible += 1

print(visible)
                