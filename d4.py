grid = open('d4.txt', 'r').read().strip().split('\n')

sum1 = 0
sum2 = 0

num_rows = len(grid)
num_cols = len(grid[0])

for row in range(num_rows):
    for col in range(num_cols):
        if col + 3 < num_cols and grid[row][col] == 'X' and grid[row][col+1] == 'M' and grid[row][col+2] == 'A' and grid[row][col+3] == 'S':
            sum1 += 1
        if row + 3 < num_rows and grid[row][col] == 'X' and grid[row+1][col] == 'M' and grid[row+2][col] == 'A' and grid[row+3][col] == 'S':
            sum1 += 1
        if row + 3 < num_rows and col + 3 < num_cols and grid[row][col] == 'X' and grid[row+1][col+1] == 'M' and grid[row+2][col+2] == 'A' and grid[row+3][col+3] == 'S':
            sum1 += 1
        if col + 3 < num_cols and grid[row][col] == 'S' and grid[row][col+1] == 'A' and grid[row][col+2] == 'M' and grid[row][col+3] == 'X':
            sum1 += 1
        if row + 3 < num_rows and grid[row][col] == 'S' and grid[row+1][col] == 'A' and grid[row+2][col] == 'M' and grid[row+3][col] == 'X':
            sum1 += 1
        if row + 3 < num_rows and col + 3 < num_cols and grid[row][col] == 'S' and grid[row+1][col+1] == 'A' and grid[row+2][col+2] == 'M' and grid[row+3][col+3] == 'X':
            sum1 += 1
        if row - 3 >= 0 and col + 3 < num_cols and grid[row][col] == 'S' and grid[row-1][col+1] == 'A' and grid[row-2][col+2] == 'M' and grid[row-3][col+3] == 'X':
            sum1 += 1
        if row - 3 >= 0 and col + 3 < num_cols and grid[row][col] == 'X' and grid[row-1][col+1] == 'M' and grid[row-2][col+2] == 'A' and grid[row-3][col+3] == 'S':
            sum1 += 1

        if row + 2 < num_rows and col + 2 < num_cols:
            if grid[row][col] == 'M' and grid[row+1][col+1] == 'A' and grid[row+2][col+2] == 'S' and grid[row+2][col] == 'M' and grid[row][col+2] == 'S':
                sum2 += 1
            if grid[row][col] == 'M' and grid[row+1][col+1] == 'A' and grid[row+2][col+2] == 'S' and grid[row+2][col] == 'S' and grid[row][col+2] == 'M':
                sum2 += 1
            if grid[row][col] == 'S' and grid[row+1][col+1] == 'A' and grid[row+2][col+2] == 'M' and grid[row+2][col] == 'M' and grid[row][col+2] == 'S':
                sum2 += 1
            if grid[row][col] == 'S' and grid[row+1][col+1] == 'A' and grid[row+2][col+2] == 'M' and grid[row+2][col] == 'S' and grid[row][col+2] == 'M':
                sum2 += 1

print(sum1)
print(sum2)
