import numpy as np

filename = "input.txt"

move_x = 3
move_y = 1


def main():
    with open(filename) as f:
        arr = np.array([list(l.strip()) for l in f])

    # assumes that numcols < numrows
    idx_row = [row for row in range(arr.shape[0])]
    idx_col = [(row * move_x) % arr.shape[1] for row in range(arr.shape[0])]

    print((arr[idx_row, idx_col] == "#").sum())


if __name__ == "__main__":
    main()
