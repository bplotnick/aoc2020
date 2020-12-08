class Instruction:
    def __init__(self, line):
        self.op, val = line.split()
        self.val = int(val)
        self.prev = set()
        self.next = None
        self.terminates = False


# create list of instruction with where they point to


def forward_pass(instructions):
    # mutates instructions and returns a list of starting instructions for DFS
    end_inst = Instruction("nop +0")
    end_inst.terminates = True
    # First find the problem instruction
    # Do forward pass to set next pointers
    for idx, inst in enumerate(instructions):
        if inst.op == "jmp":
            inst.next = idx + inst.val
        else:
            inst.next = idx + 1

        if inst.next >= len(instructions):
            end_inst.prev.add(idx)
            print(idx, inst.op, inst.val)
        else:
            instructions[inst.next].prev.add(idx)
    return end_inst


def dfs_inst(instructions, cur_inst):
    cur_inst.terminates = True
    for inst in cur_inst.prev:
        dfs_inst(instructions, instructions[inst])


def main():
    with open("input.txt") as f:
        instructions = [Instruction(l) for l in f.readlines()]

    end_inst = forward_pass(instructions)

    dfs_inst(instructions, end_inst)

    visited = {}

    PC = 0
    while True:
        if PC in visited:
            break
        cur_inst = instructions[PC]
        visited[PC] = cur_inst
        PC = cur_inst.next

    for i in visited.values():
        if i.op == "nop":
            candidate = i.next + i.val - 1
        elif i.op == "jmp":
            candidate = i.next - i.val + 1
        else:
            continue
        if instructions[candidate].terminates:
            print(f"bad instruction: {i.op} {i.val}")
            i.op = "nop" if i.op == "jmp" else "jmp"
            i.next = candidate

    PC = 0
    accumulator = 0
    while PC < len(instructions):
        cur_inst = instructions[PC]
        if cur_inst.op == "acc":
            accumulator += cur_inst.val
        PC = cur_inst.next

    print(accumulator)


#        if cur_inst.next >= len(lines):
#            cur_inst.terminates = True
#            print(f"{cur_inst} terminates")


main()
