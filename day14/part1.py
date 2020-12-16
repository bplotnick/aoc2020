def masked_val(val, mask):
    binstr = list(format(val, "036b"))
    for i, v in mask:
        binstr[i] = str(v)
    return int("".join(binstr), 2)


def convert_mask(mask_str):
    # converts from a str to indexed tuple form
    mask = []
    for idx, c in enumerate(mask_str):
        if c != "X":
            mask.append((idx, int(c)))
    return mask


def main():
    prog = []
    with open("input.txt") as f:
        for l in f:
            line = l.split()
            prog.append((line[0], line[2]))
    mem = {}

    mask = convert_mask("X" * 36)
    for op, val in prog:
        if op == "mask":
            mask = convert_mask(val)
        else:
            # mem[1234]
            mem_addr = int(op[4:-1])
            new_val = masked_val(int(val), mask)
            mem[mem_addr] = new_val

    total = sum(mem.values())
    print(mem)
    print(total)


main()
