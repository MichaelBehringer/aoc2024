import sys
from collections import deque

def solve(input_data, use_part2_logic):
    file_queue = deque()
    space_queue = deque()
    final_positions = []
    current_position = 0
    file_id = 0

    for index, char in enumerate(input_data):
        count = int(char)
        if index % 2 == 0:
            if use_part2_logic:
                file_queue.append((current_position, count, file_id))
            for _ in range(count):
                final_positions.append(file_id)
                if not use_part2_logic:
                    file_queue.append((current_position, 1, file_id))
                current_position += 1
            file_id += 1
        else:
            space_queue.append((current_position, count))
            for _ in range(count):
                final_positions.append(None)
                current_position += 1

    for pos, size, file_id in reversed(file_queue):
        for space_index, (space_pos, space_size) in enumerate(space_queue):
            if space_pos < pos and size <= space_size:
                for i in range(size):
                    final_positions[pos + i] = None
                    final_positions[space_pos + i] = file_id
                space_queue[space_index] = (space_pos + size, space_size - size)
                break

    result = sum(index * value for index, value in enumerate(final_positions) if value is not None)
    return result

sys.setrecursionlimit(500000)
data = open("d9.txt").read().strip()

sum1 = solve(data, use_part2_logic=False)
sum2 = solve(data, use_part2_logic=True)

print(sum1)
print(sum2)
