from itertools import product
from operator import add, mul

data = open("d7.txt").read().strip()
sum1 = 0
sum2 = 0

def calculate(oppCode, a, b):
    return int(str(a) + str(b)) if oppCode == "concat" else oppCode(a, b)

def check_target_value(target, allow_concat, *numbers):
    operations = [add, mul] + (["concat"] if allow_concat else [])
    for ops in product(operations, repeat=len(numbers) - 1):
        result = numbers[0]
        for i, operation in enumerate(ops):
            result = calculate(operation, result, numbers[i + 1])
            if result > target:
                break
        if result == target:
            return True
    return False

for line in data.split("\n"):
		target_value, num_list = line.split(": ")
		target_value = int(target_value)
		numbers = list(map(int, num_list.split()))
		
		if check_target_value(target_value, False, *numbers):
				sum1 += target_value
		if check_target_value(target_value, True, *numbers):
				sum2 += target_value

print(sum1)
print(sum2)
