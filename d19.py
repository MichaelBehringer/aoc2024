import sys
import re

def parse_integers(string):
    return [int(x) for x in re.findall('-?\d+', string)]

def count_ways(words, target, memo):
    if target in memo:
        return memo[target]
    
    if not target:
        return 1
    
    total_count = 0
    for word in words:
        if target.startswith(word):
            total_count += count_ways(words, target[len(word):], memo)
    
    memo[target] = total_count
    return total_count

sys.setrecursionlimit(500000)

data = open("d19.txt", 'r').read().strip()
words_section, targets_section = data.split('\n\n')
words = words_section.split(', ')
targets = targets_section.split('\n')

memoization_cache = {}
sum1 = 0
sum2 = 0

for target in targets:
    num_ways = count_ways(words, target, memoization_cache)
    if num_ways > 0:
        sum1 += 1
    sum2 += num_ways

print(sum1)
print(sum2)
