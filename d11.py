import sys

sys.setrecursionlimit(500000)
data = [int(num) for num in open("d11.txt").read().strip().split()]

memoization_cache = {}

def recursive_solver(value, depth):
    if (value, depth) in memoization_cache:
        return memoization_cache[(value, depth)]
    
    if depth == 0:
        result = 1
    elif value == 0:
        result = recursive_solver(1, depth - 1)
    elif len(str(value)) % 2 == 0:
        str_value = str(value)
        mid = len(str_value) // 2
        left_part, right_part = int(str_value[:mid]), int(str_value[mid:])
        result = recursive_solver(left_part, depth - 1) + recursive_solver(right_part, depth - 1)
    else:
        result = recursive_solver(value * 2024, depth - 1)
    
    memoization_cache[(value, depth)] = result
    return result

print(sum(recursive_solver(num, 25) for num in data))
print(sum(recursive_solver(num, 75) for num in data))
