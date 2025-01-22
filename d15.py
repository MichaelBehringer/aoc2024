import sys
import re
from collections import deque

sys.setrecursionlimit(500000)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def parse_integers(input_str):
    return [int(x) for x in re.findall('-?\d+', input_str)]

data = open("d15.txt").read().strip()

def solve(grid_data, is_part_two):
    grid, instructions = grid_data.split('\n\n')
    grid = grid.split('\n')

    rows = len(grid)
    cols = len(grid[0])
    grid = [[grid[r][c] for c in range(cols)] for r in range(rows)]

    if is_part_two:
        expanded_grid = []
        for r in range(rows):
            expanded_row = []
            for c in range(cols):
                if grid[r][c] == '#':
                    expanded_row.extend(['#', '#'])
                elif grid[r][c] == 'O':
                    expanded_row.extend(['[', ']'])
                elif grid[r][c] == '.':
                    expanded_row.extend(['.', '.'])
                elif grid[r][c] == '@':
                    expanded_row.extend(['@', '.'])
            expanded_grid.append(expanded_row)
        grid = expanded_grid
        cols *= 2

    start_row, start_col = None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                start_row, start_col = r, c
                grid[r][c] = '.'

    current_row, current_col = start_row, start_col
    direction_map = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

    for instruction in instructions:
        if instruction == '\n':
            continue

        delta_row, delta_col = direction_map[instruction]
        next_row, next_col = current_row + delta_row, current_col + delta_col

        if grid[next_row][next_col] == '#':
            continue
        elif grid[next_row][next_col] == '.':
            current_row, current_col = next_row, next_col
        elif grid[next_row][next_col] in ['[', ']', 'O']:
            to_process = deque([(current_row, current_col)])
            seen = set()
            valid_path = True

            while to_process:
                rr, cc = to_process.popleft()

                if (rr, cc) in seen:
                    continue

                seen.add((rr, cc))
                next_rr, next_cc = rr + delta_row, cc + delta_col

                if grid[next_rr][next_cc] == '#':
                    valid_path = False
                    break

                if grid[next_rr][next_cc] == 'O':
                    to_process.append((next_rr, next_cc))
                if grid[next_rr][next_cc] == '[':
                    to_process.append((next_rr, next_cc))
                    assert grid[next_rr][next_cc + 1] == ']'
                    to_process.append((next_rr, next_cc + 1))
                if grid[next_rr][next_cc] == ']':
                    to_process.append((next_rr, next_cc))
                    assert grid[next_rr][next_cc - 1] == '['
                    to_process.append((next_rr, next_cc - 1))

            if not valid_path:
                continue

            while seen:
                for rr, cc in sorted(seen):
                    next_rr, next_cc = rr + delta_row, cc + delta_col
                    if (next_rr, next_cc) not in seen:
                        assert grid[next_rr][next_cc] == '.'
                        grid[next_rr][next_cc] = grid[rr][cc]
                        grid[rr][cc] = '.'
                        seen.remove((rr, cc))

            current_row += delta_row
            current_col += delta_col

    result = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in ['[', 'O']:
                result += 100 * r + c

    return result

print(solve(data, False))
print(solve(data, True))
