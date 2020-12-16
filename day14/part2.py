from functools import lru_cache


@lru_cache
def get_replacements(binstr, mask):
    if not binstr:
        return [binstr]
    replacements = []
    idx = mask.find("X")
    if idx == -1:
        return [binstr]

    prefix = binstr[:idx]

    sub_replacements = get_replacements(binstr[idx + 1 :], mask[idx + 1 :])
    for r in sub_replacements:
        replacements.append(prefix + "0" + r)
        replacements.append(prefix + "1" + r)
    return replacements


def masked_val(val, mask):
    binstr = format(val, "036b")
    for idx, c in enumerate(mask):
        if c == "1":
            binstr = binstr[:idx] + str(c) + binstr[idx + 1 :]

    replacements = get_replacements(binstr, mask)

    return replacements


def main():
    prog = []
    with open("input.txt") as f:
        for l in f:
            line = l.split()
            prog.append((line[0], line[2]))
    mem = {}

    mask = "X" * 36
    for op, val in prog:
        if op == "mask":
            mask = val
        else:
            # mem[1234]
            mem_addrs = masked_val(int(op[4:-1]), mask)
            for addr in mem_addrs:
                mem[int(addr, 2)] = int(val)

    total = sum(mem.values())
    print(mem)
    print(total)


main()
