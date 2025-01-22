import sys
from collections import deque

def connected_components(grid, start_row, start_col, visited, directions):
    queue = deque([(start_row, start_col)])
    area = 0
    perimeter = 0
    perimeter_cells = {}

    while queue:
        r, c = queue.popleft()
        if (r, c) in visited:
            continue
        
        visited.add((r, c))
        area += 1

        for dr, dc in directions:
            rr, cc = r + dr, c + dc
            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]) and grid[rr][cc] == grid[r][c]:
                queue.append((rr, cc))
            else:
                perimeter += 1
                if (dr, dc) not in perimeter_cells:
                    perimeter_cells[(dr, dc)] = set()
                perimeter_cells[(dr, dc)].add((r, c))
    
    sides = count_sides(perimeter_cells, directions)
    return area, perimeter, sides

def count_sides(perimeter_cells, directions):
    sides = 0
    for direction, cells in perimeter_cells.items():
        visited_perimeter = set()
        for pr, pc in cells:
            if (pr, pc) not in visited_perimeter:
                sides += 1
                queue = deque([(pr, pc)])
                while queue:
                    r, c = queue.popleft()
                    if (r, c) in visited_perimeter:
                        continue
                    visited_perimeter.add((r, c))
                    for dr, dc in directions:
                        if (r + dr, c + dc) in cells:
                            queue.append((r + dr, c + dc))
    return sides


sys.setrecursionlimit(500000)
data = open("d12.txt").read().strip().split('\n')
rows, cols = len(data), len(data[0])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = set()
sum1 = 0
sum2 = 0

for r in range(rows):
    for c in range(cols):
        if (r, c) not in visited:
            area, perimeter, sides = connected_components(data, r, c, visited, directions)
            sum1 += area * perimeter
            sum2 += area * sides

print(sum1)
print(sum2)
