def get_instructions(file_name):
    instructions = []
    
    with open(file_name) as f:
        for instruction in f:
            instructions += [instruction.replace("\n", "")]

    return instructions 

def get_accumulator_value(instructions):
    executed_instructions = []
    accumulator_value = 0
    index = 0
    while index >= 0 and index not in executed_instructions and index < len(instructions):
        executed_instructions += [index]
        instruction = instructions[index]
        instruction_parts = instruction.split(" ")
        if instruction_parts[0] == "nop":
            index += 1
        elif instruction_parts[0] == "acc":
            index += 1
            accumulator_value += (int) (instruction_parts[1])
        else:
            index += (int) (instruction_parts[1])
    
    return (index in executed_instructions, accumulator_value)

def get_good_instructions(instructions):
    changed_jmp_or_nop_indexes = []
    for i in range(0, len(instructions)):
        instruction_name = instructions[i].split(" ")[0]
        if instruction_name == "jmp" or instruction_name == "nop":
            changed_jmp_or_nop_indexes += [i]

    for index in changed_jmp_or_nop_indexes:
        instructions_copy = instructions.copy()
        instruction_to_change = instructions_copy[index]
        if instruction_to_change.split(" ")[0] == "jmp":
            instructions_copy[index] = instruction_to_change.replace("jmp", "nop")
        else:
            instructions_copy[index] = instruction_to_change.replace("nop", "jmp")
        result_instruction = get_accumulator_value(instructions_copy)
        if not result_instruction[0]:
            return result_instruction

def main():
    print("---___---")
    instructions = get_instructions("input.txt")
    accumulator_value = get_accumulator_value(instructions)
    print("1st star")
    print(accumulator_value)
    good_acumulator_value = get_good_instructions(instructions)
    print("2nd star")
    print(good_acumulator_value)

if __name__ == "__main__":
    main()