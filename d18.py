from queue import Queue

def find_shortest_path(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = Queue()
    queue.put((start, [start]))
    visited = set([start])
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while not queue.empty():
        (current_x, current_y), path = queue.get()
        
        if (current_x, current_y) == goal:
            return path
        
        for dx, dy in moves:
            next_x, next_y = current_x + dx, current_y + dy
            if (0 <= next_x < rows and 0 <= next_y < cols and 
                grid[next_x][next_y] == 0 and (next_x, next_y) not in visited):
                queue.put(((next_x, next_y), path + [(next_x, next_y)]))
                visited.add((next_x, next_y))
    
    return None

grid_size = 71
grid = []
for _ in range(grid_size):
    row = [0] * grid_size
    grid.append(row)

data = open("d18.txt", 'r')
for i, line in enumerate(data):
        x, y = map(int, line.strip().split(','))
        grid[x][y] = 1
        
        if i > 1024:
                path = find_shortest_path(grid, (0, 0), (70, 70))
                if i == 1025:
                        print(len(path) - 1)
                if not path:
                        print(f"{x},{y}")
                        break