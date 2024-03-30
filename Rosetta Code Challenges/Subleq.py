# Subleq
def subleq_interpreter(memory):
    output = ""
    instruction_pointer = 0
    while True:
        A = memory[instruction_pointer]
        B = memory[instruction_pointer + 1]
        C = memory[instruction_pointer + 2]
        instruction_pointer += 3
        if A == -1:
            memory[B] = ord(input("Input a character: ")[0])
        elif B == -1:
            output += chr(memory[A])
        else:
            memory[B] -= memory[A]
            if memory[B] <= 0:
                instruction_pointer = C
        if instruction_pointer < 0:
            break
    return output
program = [15, 17, -1, 17, -1, -1, 16, 1, -1, 16, 3, -1, 15, 15, 0, 0, -1, 72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33, 10, 0]
output = subleq_interpreter(program)
print(output)