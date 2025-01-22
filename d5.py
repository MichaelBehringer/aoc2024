from collections import defaultdict

order_data, update_data = open('d5.txt').read().split('\n\n')
updates = [list(map(int, line.split(','))) for line in update_data.splitlines()]

page_dependencies = defaultdict(list)
for order in order_data.splitlines():
    before_page, after_page = map(int, order.split('|'))
    page_dependencies[before_page].append(after_page)

middle_sum_1 = 0
middle_sum_2 = 0

for update_pages in updates:
    sorted_pages = sorted(
        update_pages,
        key=lambda page: -len(set(page_dependencies[page]).intersection(update_pages))
    )
    if update_pages == sorted_pages:
        middle_sum_1 += update_pages[len(update_pages) // 2]
    else:
        middle_sum_2 += sorted_pages[len(sorted_pages) // 2]

print(middle_sum_1)
print(middle_sum_2)
