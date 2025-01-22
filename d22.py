data = [int(line) for line in open('d22.txt').read().strip().split('\n')]

sum = 0
pattern_frequencies = {}

for number in data:
    sequence = [0] * (2000+1)
    sequence[0] = number % 10

    for i in range(1, 2000+1):
        number = (number ^ (number * 64)) % 16777216
        number = (number ^ (number // 32)) % 16777216
        number = (number ^ (number * 2048)) % 16777216
        sequence[i] = number % 10

    sum += number
    
    differences = [sequence[i] - sequence[i - 1] for i in range(1, 2000+1)]
    seen_patterns = set()

    for index in range(3, len(differences)):
        pattern = tuple(differences[index - 3 : index + 1])
        if pattern not in seen_patterns:
            pattern_frequencies[pattern] = pattern_frequencies.get(pattern, 0) + sequence[index + 1]
            seen_patterns.add(pattern)

print(sum)
print(max(pattern_frequencies.values()))
