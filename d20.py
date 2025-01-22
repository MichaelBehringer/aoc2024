def get_neighbors(x, y):
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

def is_valid_position(nx, ny, track, grid):
    return (nx, ny) != track[-2] and grid[ny][nx] != '#'

def find_next_position(x, y, track, grid):
    return next(
        (nx, ny) 
        for nx, ny in get_neighbors(x, y) 
        if is_valid_position(nx, ny, track, grid)
    )

def parse_track(file):
    grid = [line.strip() for line in file]
    
    start_position = next(
        (x, y)
        for y, row in enumerate(grid)
        for x, cell in enumerate(row)
        if cell == 'S'
    )
    
    x, y = start_position
    track = [None, (x, y)]
    
    while grid[y][x] != 'E':
        next_position = find_next_position(x, y, track, grid)
        track.append(next_position)
        x, y = next_position
    
    return track[1:]

def find_cheats(track, max_distance):
    for index1, (x1, y1) in enumerate(track):
        for index2 in range(index1 + 3, len(track)):
            x2, y2 = track[index2]
            distance = abs(x2 - x1) + abs(y2 - y1)
            
            if distance <= max_distance and index2 - index1 > distance:
                yield (index2 - index1 - distance)


data = parse_track(open("d20.txt", 'r'))

sum1 = len([saved for saved in find_cheats(data, 2) if saved >= 100])
sum2 = len([saved for saved in find_cheats(data, 20) if saved >= 100])

print(sum1)
print(sum2)
