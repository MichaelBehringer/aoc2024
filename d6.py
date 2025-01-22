import sys
sys.setrecursionlimit(500000)

data = open("d6.txt").read().strip()

grid = [list(row) for row in data.split("\n")]
rows, cols = len(grid), len(grid[0])

start_x, start_y = 0, 0
for x in range(rows):
    for y in range(cols):
        if grid[x][y] in ">^v<":
            start_x, start_y = x, y

movement_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

current_x, current_y, current_dir = start_x, start_y, 0
visited_positions = set()

while 0 <= current_x < rows and 0 <= current_y < cols:
    visited_positions.add((current_x, current_y))
    while True:
        dx, dy = movement_directions[current_dir]
        next_x, next_y = current_x + dx, current_y + dy
        if 0 <= next_x < rows and 0 <= next_y < cols and grid[next_x][next_y] == "#":
            current_dir = (current_dir + 1) % 4
        else:
            current_x, current_y = next_x, next_y
            break

print(len(visited_positions))

loop_count = 0

for obstacle_x in range(rows):
    for obstacle_y in range(cols):
        if grid[obstacle_x][obstacle_y] in "#^":
            continue

        grid[obstacle_x][obstacle_y] = "#"
        visited_positions = set()
        current_x, current_y, current_dir = start_x, start_y, 0

        while (
            0 <= current_x < rows and 0 <= current_y < cols and (current_x, current_y, current_dir) not in visited_positions
        ):
            visited_positions.add((current_x, current_y, current_dir))
            while True:
                dx, dy = movement_directions[current_dir]
                next_x, next_y = current_x + dx, current_y + dy
                if 0 <= next_x < rows and 0 <= next_y < cols and grid[next_x][next_y] == "#":
                    current_dir = (current_dir + 1) % 4
                else:
                    current_x, current_y = next_x, next_y
                    break

        if (current_x, current_y, current_dir) in visited_positions:
            loop_count += 1

        grid[obstacle_x][obstacle_y] = "."

print(loop_count)
