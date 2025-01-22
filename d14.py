import sys
import re
from collections import deque

sys.setrecursionlimit(500000)

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def parse_integers(s):
    return [int(x) for x in re.findall(r'-?\d+', s)]
data = open("d14.txt").read().strip()

GRID_WIDTH = 101
GRID_HEIGHT = 103

robots = []
quadrant_counts = [0, 0, 0, 0]

def initialize_robots(data):
    robots = []
    for line in data.split('\n'):
        px, py, vx, vy = parse_integers(line)
        robots.append((px, py, vx, vy))
    return robots

robots = initialize_robots(data)

def update_robot_positions(robots, grid_width, grid_height):
    for i, (px, py, vx, vy) in enumerate(robots):
        px = (px + vx) % grid_width
        py = (py + vy) % grid_height
        robots[i] = (px, py, vx, vy)
    return robots

def create_grid(width, height):
    return [['.' for _ in range(width)] for _ in range(height)]

def count_quadrants(robots, grid_width, grid_height):
    mid_x, mid_y = grid_width // 2, grid_height // 2
    counts = [0, 0, 0, 0]

    for px, py, _, _ in robots:
        if px < mid_x and py < mid_y:
            counts[0] += 1 
        elif px >= mid_x and py < mid_y:
            counts[1] += 1
        elif px < mid_x and py >= mid_y:
            counts[2] += 1
        elif px >= mid_x and py >= mid_y:
            counts[3] += 1
    return counts

def count_components(grid, directions):
    seen = set()
    components = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '#' and (x, y) not in seen:
                components += 1
                queue = deque([(x, y)])

                while queue:
                    cx, cy = queue.popleft()
                    if (cx, cy) in seen:
                        continue
                    seen.add((cx, cy))

                    for dx, dy in directions:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == '#':
                            queue.append((nx, ny))
    return components


for time in range(1, 10**6):
		grid = create_grid(GRID_WIDTH, GRID_HEIGHT)
		robots = update_robot_positions(robots, GRID_WIDTH, GRID_HEIGHT)

		for px, py, _, _ in robots:
				grid[py][px] = '#'

		if time == 100:
				quadrant_counts[:] = count_quadrants(robots, GRID_WIDTH, GRID_HEIGHT)
				p1 = quadrant_counts[0] * quadrant_counts[1] * quadrant_counts[2] * quadrant_counts[3]
				print(p1)

		components = count_components(grid, DIRECTIONS)

		if components <= 200:
				print(time)
