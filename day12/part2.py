import numpy as np
from functools import reduce

directions = ["E", "S", "W", "N"]
translations = {
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
    "N": (-1, 0),
}
rotations = {
    "L": 1,
    "R": -1,
}

# 90 degree counterclockwise rotation
rotation_matrix = np.array([[0, -1], [1, 0]])


def do_one(cur_pos, cur_waypoint, inst):
    op = inst[0]
    val = inst[1:]
    # returns new pos and dir
    new_pos = cur_pos
    new_waypoint = cur_waypoint
    if op in translations.keys():
        new_waypoint += np.array(
            [
                int(val) * translations[op][0],
                int(val) * translations[op][1],
            ]
        )
    elif op in rotations.keys():
        rot_mat = reduce(np.dot, [rotations[op] * rotation_matrix] * (int(val) // 90))
        new_waypoint = np.dot(rot_mat, cur_waypoint)
    else:
        assert op == "F"
        new_pos += np.array(
            [
                int(val) * new_waypoint[0],
                int(val) * new_waypoint[1],
            ]
        )
    return new_pos, new_waypoint


def main():
    with open("input.txt") as f:
        instructions = f.readlines()

    waypoint = np.array([-1, 10])
    cur_pos = np.array([0, 0])
    for inst in instructions:
        cur_pos, waypoint = do_one(cur_pos, waypoint, inst)
        print(inst, cur_pos, waypoint)
    print(abs(cur_pos[0]) + abs(cur_pos[1]))


main()
