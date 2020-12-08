def main():
    with open("input.txt") as f:
        lines = [l.split() for l in f.readlines()]
    visited = [False] * len(lines)
    PC = 0
    accumulator = 0
    while True:
        if visited[PC] == True:
            print(accumulator)
            return
        print(PC, lines[PC])
        op, val = lines[PC]
        visited[PC] = True
        if op == "nop":
            PC += 1
        elif op == "acc":
            accumulator += int(val)
            PC += 1
        elif op == "jmp":
            PC += int(val)
        else:
            raise ValueError(f"unknown op {op}")


main()
