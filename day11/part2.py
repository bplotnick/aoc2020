import numpy as np

DIRECTIONS = {
    "l": (0, -1),
    "ul": (-1, -1),
    "u": (-1, 0),
    "ur": (-1, 1),
    "r": (0, 1),
    "br": (1, 1),
    "b": (1, 0),
    "bl": (1, -1),
}


def _walk_direction(board, start, direction):
    found = False
    cur_cell = (
        start[0] + DIRECTIONS[direction][0],
        start[1] + DIRECTIONS[direction][1],
    )
    while 0 <= cur_cell[0] < board.shape[0] and 0 <= cur_cell[1] < board.shape[1]:
        cur_val = board[cur_cell]
        if cur_val == "L":
            return False
        elif cur_val == "#":
            return True
        else:
            assert cur_val == "."

        cur_cell = (
            cur_cell[0] + DIRECTIONS[direction][0],
            cur_cell[1] + DIRECTIONS[direction][1],
        )
    return found


def walk_directions(board, start):
    count = 0
    for direction in DIRECTIONS.keys():
        count += _walk_direction(board, start, direction)
    return count


def main():
    data = np.loadtxt(
        "input.txt", dtype="str", converters={0: lambda x: list(x.decode("utf-8"))}
    )
    new_data = data.copy()
    while True:
        # print('\n')
        # print(data)
        for index, x in np.ndenumerate(data):
            if x == ".":
                continue
            count = walk_directions(data, index)
            if x == "#" and count >= 5:
                new_data[index] = "L"
            elif x == "L" and count == 0:
                new_data[index] = "#"
            else:
                continue
        if np.array_equal(new_data, data):
            print(np.count_nonzero(data == "#"))
            return
        data = new_data.copy()


main()
