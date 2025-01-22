import os
import sys

nummern_keypad = {
    "7": (0, 0), "8": (1, 0), "9": (2, 0),
    "4": (0, 1), "5": (1, 1), "6": (2, 1),
    "1": (0, 2), "2": (1, 2), "3": (2, 2),
    "0": (1, 3), "A": (2, 3)
}

richtungs_keypad = {
    "^": (1, 0), "A": (2, 0), "<": (0, 1),
    "v": (1, 1), ">": (2, 1)
}

def generate_keypad_sequence(use_alternate, positions, code, start_x, start_y):
    sequence = ""
    for char in code:
        target_x, target_y = positions[char]
        dx = target_x - start_x
        dy = target_y - start_y

        if use_alternate:
            if dx == 2 and dy > 0 and target_y == 3:
                sequence += ">" * dx + "v" * dy
            elif dx == -2 and dy < 0 and start_y == 3:
                sequence += "^" * abs(dy) + "<<"
            elif dx == -1 and start_x == 1 and dy < 0 and start_y == 3:
                sequence += "^" * abs(dy) + "<"
            else:
                sequence += move(dx, dy)
        else:
            sequence += handle_non_alternate(dx, dy, start_x, start_y)

        sequence += "A"
        start_x, start_y = target_x, target_y
    
    return sequence

def move(dx, dy):
    result = ""
    if dx < 0:
        result += "<" * abs(dx)
    if dy < 0:
        result += "^" * abs(dy)
    else:
        result += "v" * abs(dy)
    if dx > 0:
        result += ">" * abs(dx)
    return result

def handle_non_alternate(dx, dy, start_x, start_y):
    if dx == 2 and dy == -1:
        return ">>^"
    if dx == -2 and dy == 1:
        return "v<<"
    if dx == -1 and dy == 1 and start_x == 1 and start_y == 0:
        return "v<"
    if dx == 1 and dy == -1 and start_x == 0 and start_y == 1:
        return ">^"
    return move(dx, dy)

def count_key_sequences(sequence):
    counts = {}
    current_key = ""
    for char in sequence:
        current_key += char
        if char == "A":
            counts[current_key] = counts.get(current_key, 0) + 1
            current_key = ""
    return counts

def calculate_key_counts(use_alternate, positions, code_counts, start_x, start_y):
    new_counts = {}
    for code, occurrences in code_counts.items():
        transformed_sequence = generate_keypad_sequence(use_alternate, positions, code, start_x, start_y)
        for key, count in count_key_sequences(transformed_sequence).items():
            new_counts[key] = new_counts.get(key, 0) + count * occurrences
    return new_counts

def compute_complexity(counts):
    return sum(len(key) * count for key, count in counts.items())

data = open("d21.txt", "r").readlines()
sum1 = 0
sum2 = 0

for line in data:
    initial_counts = count_key_sequences(line)
    step1_counts = calculate_key_counts(True, nummern_keypad, initial_counts, 2, 3)

    previous_counts = step1_counts
    for iteration in range(25):
        new_counts = calculate_key_counts(False, richtungs_keypad, previous_counts, 2, 0)
        previous_counts = new_counts
        if iteration == 1:
            sum1 += compute_complexity(new_counts) * int(line[:3])
    
    sum2 += compute_complexity(previous_counts) * int(line[:3])

print(sum1)
print(sum2)
