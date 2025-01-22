from collections import defaultdict
from itertools import combinations

grid = open("d8.txt", "r").read().splitlines()

antennas = defaultdict(list)
for row_index, row in enumerate(grid):
    for col_index, cell in enumerate(row):
        if cell != ".":
            antennas[cell].append((row_index, col_index))

def calculate_antinode_positions(pos1, pos2, extend_search=False):
    row1, col1 = pos1
    row2, col2 = pos2
    
    row_diff = row1 - row2
    col_diff = col1 - col2
    
    antinodes = {(row1, col1), (row2, col2)} if extend_search else set()

    while 0 <= row1 + row_diff < len(grid) and 0 <= col1 + col_diff < len(grid[0]):
        row1 += row_diff
        col1 += col_diff
        antinodes.add((row1, col1))
        if not extend_search:
            break

    while 0 <= row2 - row_diff < len(grid) and 0 <= col2 - col_diff < len(grid[0]):
        row2 -= row_diff
        col2 -= col_diff
        antinodes.add((row2, col2))
        if not extend_search:
            break

    return antinodes


unique_antinodes = set()
for antenna_positions in antennas.values():
		for pos1, pos2 in combinations(antenna_positions, 2):
				unique_antinodes.update(calculate_antinode_positions(pos1, pos2))
print(len(unique_antinodes))

unique_antinodes = set()
for antenna_positions in antennas.values():
		for pos1, pos2 in combinations(antenna_positions, 2):
				unique_antinodes.update(calculate_antinode_positions(pos1, pos2, extend_search=True))
print(len(unique_antinodes))
