import re

def solve_linear_system(vector_a, vector_b, point_p, delta=0):
    ax, ay = vector_a
    bx, by = vector_b
    px, py = point_p

    px += delta
    py += delta

    denominator = ax * by - ay * bx
    n1 = (px * by - py * bx) / denominator
    n2 = (py * ax - px * ay) / denominator

    return n1, n2

def parse_input():
    data = open("d13.txt").read().strip().split("\n\n")

    machines = []
    for group in data:
        values = list(map(int, re.findall(r"\d+", group)))
        machines.append(((values[0], values[1]), (values[2], values[3]), (values[4], values[5])))

    return machines

def calculate_tokens(machines, delta=0, range_limit=100):
    tokens = 0

    for machine in machines:
        vector_a, vector_b, point_p = machine
        n1, n2 = solve_linear_system(vector_a, vector_b, point_p, delta)

        if n1.is_integer() and n2.is_integer():
            n1, n2 = int(n1), int(n2)
            if 0 <= n1 < range_limit and 0 <= n2 < range_limit:
                tokens += (3 * n1 + n2)

    return tokens


input = parse_input()
print(calculate_tokens(input))
print(calculate_tokens(input, delta=10**13, range_limit=9999999999999999))