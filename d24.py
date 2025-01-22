wire_register = {}
pending_operations = []
file_content = open("d24.txt").read().splitlines()
largest_z_key = "z00"

def compute_binary_operation(op_type, val1, val2):
    operations_map = {
        "XOR": val1 ^ val2,
        "OR": val1 | val2,
        "AND": val1 & val2,
    }
    return operations_map[op_type]

for line in file_content:
    if ":" in line:
        key, value = line.split(": ")
        wire_register[key] = int(value)
    elif "->" in line:
        part1, operator, part2, _, result = line.split(" ")
        pending_operations.append((part1, operator, part2, result))

flagged_wires = set()
for part1, op_type, part2, result in pending_operations:
    if result.startswith("z") and op_type != "XOR" and result != "z45":
        flagged_wires.add(result)
    
    if op_type == "XOR" and not any(w[0] in "xyz" for w in [result, part1, part2]):
        flagged_wires.add(result)
    
    if op_type == "AND" and "x00" not in {part1, part2}:
        for inner1, inner_op, inner2, inner_result in pending_operations:
            if result in {inner1, inner2} and inner_op != "OR":
                flagged_wires.add(result)
    
    if op_type == "XOR":
        for inner1, inner_op, inner2, inner_result in pending_operations:
            if result in {inner1, inner2} and inner_op == "OR":
                flagged_wires.add(result)

while pending_operations:
    part1, operation, part2, output = pending_operations.pop(0)
    if part1 in wire_register and part2 in wire_register:
        wire_register[output] = compute_binary_operation(operation, wire_register[part1], wire_register[part2])
    else:
        pending_operations.append((part1, operation, part2, output))

binary_values = [str(wire_register[k]) for k in sorted(wire_register, reverse=True) if k.startswith("z")]

print(int("".join(binary_values), 2))
print(",".join(sorted(flagged_wires)))
