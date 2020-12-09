import numpy as np

window_size = 25


def main():
    data = np.loadtxt("input.txt", dtype=int)
    i = window_size
    while i < data.shape[0]:
        cur_window = data[i - window_size : i]
        subtracted = data[i] - cur_window
        common = np.intersect1d(cur_window, subtracted)
        if len(common) == 0:
            print(cur_window, subtracted)
            print(f"Found index value {data[i]} at index {i}")
            return
        i += 1


main()
