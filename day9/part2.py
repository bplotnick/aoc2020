import numpy as np

window_size = 25


def find_bad_num(data):
    i = window_size
    while i < data.shape[0]:
        cur_window = data[i - window_size : i]
        subtracted = data[i] - cur_window
        common = np.intersect1d(cur_window, subtracted)
        if len(common) == 0:
            return i
        i += 1


def main():
    data = np.loadtxt("input.txt", dtype=int)
    bad_num_idx = find_bad_num(data)
    bad_num = data[bad_num_idx]

    i_l = 0
    i_r = 1
    total = data[i_l] + data[i_r]
    while i_r < bad_num_idx:
        if total == bad_num:
            smol = data[i_l : i_r + 1].min()
            thicc = data[i_l : i_r + 1].max()
            print(smol + thicc)
            return
        elif total < bad_num:
            i_r += 1
            total += data[i_r]
        elif total > bad_num:
            total -= data[i_l]
            i_l += 1
        else:
            raise Exception("wat")


main()
