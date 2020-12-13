directions = ["E", "S", "W", "N"]
translations = {
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
    "N": (-1, 0),
}
rotations = {
    "L": -1,
    "R": 1,
}


def do_one(cur_pos, cur_dir, inst):
    op = inst[0]
    val = inst[1:]
    # returns new pos and dir
    new_pos = cur_pos
    new_dir = cur_dir
    if op in translations.keys():
        new_pos = (
            cur_pos[0] + int(val) * translations[op][0],
            cur_pos[1] + int(val) * translations[op][1],
        )
    elif op in rotations.keys():
        new_dir = (cur_dir + rotations[op] * (int(val) // 90)) % len(directions)
    else:
        assert op == "F"
        tran = translations[directions[cur_dir]]
        new_pos = (
            cur_pos[0] + int(val) * tran[0],
            cur_pos[1] + int(val) * tran[1],
        )
    return new_pos, new_dir


def main():
    with open("input.txt") as f:
        instructions = f.readlines()

    cur_pos = (0, 0)
    cur_dir = 0  # East
    for inst in instructions:
        cur_pos, cur_dir = do_one(cur_pos, cur_dir, inst)
    print(abs(cur_pos[0]) + abs(cur_pos[1]))


main()
