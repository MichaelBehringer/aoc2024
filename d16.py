import sys
import heapq
import pyperclip as pc

def parse_input():
    data = open("d16.txt", 'r').read().strip().split('\n')
    rows = len(data)
    cols = len(data[0])
    return [[cell for cell in row] for row in data], rows, cols

def find_start_end_positions(grid):
    start = end = None
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'S':
                start = (row, col)
            elif grid[row][col] == 'E':
                end = (row, col)
    return start, end

def dijkstra(grid, rows, cols, start, end, directions):
    queue = []
    seen = set()
    distances = {}
    heapq.heappush(queue, (0, *start, 1))
    best_distance = None

    while queue:
        dist, row, col, direction = heapq.heappop(queue)

        if (row, col, direction) not in distances:
            distances[(row, col, direction)] = dist

        if (row, col) == end and best_distance is None:
            best_distance = dist

        if (row, col, direction) in seen:
            continue
        seen.add((row, col, direction))

        dr, dc = directions[direction]
        next_row, next_col = row + dr, col + dc

        if 0 <= next_col < cols and 0 <= next_row < rows and grid[next_row][next_col] != '#':
            heapq.heappush(queue, (dist + 1, next_row, next_col, direction))

        heapq.heappush(queue, (dist + 1000, row, col, (direction + 1) % 4))
        heapq.heappush(queue, (dist + 1000, row, col, (direction + 3) % 4))

    return best_distance, distances

def reverse_dijkstra(grid, rows, cols, end, directions):
    queue = []
    seen = set()
    distances = {}

    for direction in range(4):
        heapq.heappush(queue, (0, *end, direction))

    while queue:
        dist, row, col, direction = heapq.heappop(queue)

        if (row, col, direction) not in distances:
            distances[(row, col, direction)] = dist

        if (row, col, direction) in seen:
            continue
        seen.add((row, col, direction))

        dr, dc = directions[(direction + 2) % 4]
        next_row, next_col = row + dr, col + dc

        if 0 <= next_col < cols and 0 <= next_row < rows and grid[next_row][next_col] != '#':
            heapq.heappush(queue, (dist + 1, next_row, next_col, direction))

        heapq.heappush(queue, (dist + 1000, row, col, (direction + 1) % 4))
        heapq.heappush(queue, (dist + 1000, row, col, (direction + 3) % 4))

    return distances

def find_optimal_paths(grid, rows, cols, start, end, directions):
    best_distance, distances_from_start = dijkstra(grid, rows, cols, start, end, directions)
    distances_to_end = reverse_dijkstra(grid, rows, cols, end, directions)

    optimal_positions = set()
    for row in range(rows):
        for col in range(cols):
            for direction in range(4):
                if (
                    (row, col, direction) in distances_from_start
                    and (row, col, direction) in distances_to_end
                    and distances_from_start[(row, col, direction)] + distances_to_end[(row, col, direction)] == best_distance
                ):
                    optimal_positions.add((row, col))

    return best_distance, len(optimal_positions)

sys.setrecursionlimit(500000)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

grid, rows, cols = parse_input()
start, end = find_start_end_positions(grid)

p1, p2 = find_optimal_paths(grid, rows, cols, start, end, directions)

print(p1)
print(p2)
