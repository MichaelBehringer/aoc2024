import re

def parse_input(puzzle_input):
    register_section, program_section = puzzle_input.split('\n\n')
    register_values = list(map(int, re.findall(r'\d+', register_section)))
    program = [int(i) for i in re.findall(r'\d+', program_section)]
    return dict(zip('ABC', register_values)), program

def combo(register, operand):
    if operand == 4:
        return register['A']
    if operand == 5:
        return register['B']
    if operand == 6:
        return register['C']
    return operand

def execute_program(register, program):
    i = 0
    n = len(program)
    output = []
    
    while i < n:
        opcode, operand = program[i:i+2]
        match opcode:
            case 0:
                register['A'] >>= combo(register, operand)
            case 1:
                register['B'] ^= operand
            case 2:
                register['B'] = combo(register, operand) % 8
            case 3:
                if register['A']:
                    i = operand - 2
            case 4:
                register['B'] ^= register['C']
            case 5:
                output.append(combo(register, operand) % 8)
            case 6:
                register['B'] = register['A'] >> combo(register, operand)
            case 7:
                register['C'] = register['A'] >> combo(register, operand)
        i += 2
    
    return output

def part1(puzzle_input):
    register, program = parse_input(puzzle_input)
    output = execute_program(register, program)
    return ','.join(map(str, output))

def part2(puzzle_input):
    initial_register, program = parse_input(puzzle_input)
    B, C = initial_register['B'], initial_register['C']
    n = len(program)
    
    def run_with_A(A):
        register = {'A': A, 'B': B, 'C': C}
        return execute_program(register, program)
    
    A = 0
    for i in reversed(range(n)):
        A <<= 3
        while run_with_A(A) != program[i:]:
            A += 1

    return A

data = open("d17.txt", 'r').read().strip()
print(part1(data))
print(part2(data))
