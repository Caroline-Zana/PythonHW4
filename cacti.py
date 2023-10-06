def cacti_num(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                
                adjacent_empty = all(grid[x][y] == 0 for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
                diagonal_empty = all(grid[x][y] == 0 for x, y in [(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)])
                
                if adjacent_empty and diagonal_empty:
                    count += 1

    return count
