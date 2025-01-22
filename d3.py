import re

data = open('d3.txt', 'r').read().strip()

matches = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", data)

action = True
sum1 = 0
sum2 = 0

for(match) in matches:
    if match == "do()":
        action = True
    elif match == "don't()":
        action = False
    else:
        a, b = map(int, match[4:-1].split(","))
        sum1 += a * b
        if action:
            sum2 += a * b

print(sum1)
print(sum2)