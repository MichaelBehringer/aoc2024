data = open('d2.txt', 'r').read().strip().split('\n')

def is_safe(report):
    is_increasing = all(report[i] > report[i-1] for i in range(1, len(report)))
    is_decreasing = all(report[i] < report[i-1] for i in range(1, len(report)))

    if not (is_increasing or is_decreasing):
        return False

    for i in range(1, len(report)):
        diff = abs(report[i] - report[i-1])
        if diff < 1 or diff > 3:
            return False

    return True

count1 = 0
count2 = 0

for report in data:
    report_split = list(map(int, report.split()))

    if is_safe(report_split):
        count1 += 1
        count2 += 1
        continue

    safe_with_skip = False
    for i in range(len(report_split)):
        modified_report = report_split[:i] + report_split[i+1:]
        if is_safe(modified_report):
            safe_with_skip = True
            break

    if safe_with_skip:
        count2 += 1

print(count1)
print(count2)
