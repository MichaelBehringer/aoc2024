import sys
from collections import deque

def count_reachable_zeros(start_row, start_col, grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start_row, start_col)])
    seen = set()
    zero_count = 0
    
    while queue:
        r, c = queue.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        if grid[r][c] == 0:
            zero_count += 1
        
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr, cc = r + dr, c + dc
            if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == grid[r][c] - 1:
                queue.append((rr, cc))
    
    return zero_count

def count_paths_to_zero(r, c, grid, memo):
    if grid[r][c] == 0:
        return 1
    if (r, c) in memo:
        return memo[(r, c)]
    
    rows, cols = len(grid), len(grid[0])
    total_paths = 0
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        rr, cc = r + dr, c + dc
        if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == grid[r][c] - 1:
            total_paths += count_paths_to_zero(rr, cc, grid, memo)
    
    memo[(r, c)] = total_paths
    return total_paths


sys.setrecursionlimit(500000)
data = [[int(x) for x in line.strip()] for line in open("d10.txt")]
rows, cols = len(data), len(data[0])
sum1 = 0
sum2 = 0
memo = {}

for r in range(rows):
		for c in range(cols):
				if data[r][c] == 9:
						sum1 += count_reachable_zeros(r, c, data)
						sum2 += count_paths_to_zero(r, c, data, memo)

print(sum1)
print(sum2)
