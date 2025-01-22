def parse_input_file(data):
    lock_patterns = []
    key_patterns = []

    for group in data:
        lines = group.splitlines()
        pattern = tuple(column.count('#') - 1 for column in zip(*lines))

        if lines[0] == '#####':
            lock_patterns.append(pattern)
        else:
            key_patterns.append(pattern)

    return lock_patterns, key_patterns


def can_key_fit_lock(lock_pattern, key_pattern):
    return all(lock + key <= 5 for lock, key in zip(lock_pattern, key_pattern))

data = open("d25.txt", "r").read().split('\n\n')
lock_patterns, key_patterns = parse_input_file(data)

sum = sum(
		can_key_fit_lock(lock, key)
		for lock in lock_patterns
		for key in key_patterns
)

print(sum)
