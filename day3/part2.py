import logging
import numpy as np

filename = "input.txt"


def sol(arr: np.ndarray, move_x: int, move_y: int) -> int:
    num_indices = max([arr.shape[0] // move_y, arr.shape[1] // move_x])
    idx_row = [(i * move_y) % arr.shape[0] for i in range(num_indices)]
    idx_col = [(i * move_x) % arr.shape[1] for i in range(num_indices)]
    logging.debug(idx_row)
    logging.debug(idx_col)

    return (arr[idx_row, idx_col] == "#").sum()


def main():
    logging.basicConfig(level=logging.INFO)
    with open(filename) as f:
        arr = np.array([list(l.strip()) for l in f])

    inputs = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    total = 1
    for i in inputs:
        s = sol(arr, i[0], i[1])
        logging.info(f"Input {i}; sol {s}")
        total *= s
    print(total)


if __name__ == "__main__":
    main()
