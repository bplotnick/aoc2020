import numpy as np
import time
import matplotlib

matplotlib.use("macosx")
import matplotlib.pyplot as plt

THRESH = 5  # Actually 5 this time


def main():
    data = np.loadtxt(
        "small_input.txt",
        dtype="str",
        converters={0: lambda x: list(x.decode("utf-8"))},
    )

    plt.ion()
    imobj = plt.matshow(data == "#", vmin=0, vmax=1)
    plt.pause(0.001)
    while True:
        seat_indices = np.column_stack(np.where(data != "."))
        nums = np.zeros_like(data, dtype=int)
        for s in seat_indices:
            adj_vals = []
            # top
            t = data[: s[0], s[1]]
            top_idx = t[t != "."]
            if len(top_idx) > 0:
                adj_vals.append(top_idx[-1])

            # bottom
            t = data[s[0] + 1 :, s[1]]
            bot_idx = t[t != "."]
            if len(bot_idx) > 0:
                adj_vals.append(bot_idx[0])

            # left
            t = data[s[0], : s[1]]
            left_idx = t[t != "."]
            if len(left_idx) > 0:
                adj_vals.append(left_idx[-1])

            # right
            t = data[s[0], s[1] + 1 :]
            right_idx = t[t != "."]
            if len(right_idx) > 0:
                adj_vals.append(right_idx[0])

            # major diagonal, top left to bottom right
            offset = s[1] - s[0]
            diag = np.diagonal(data, offset)
            # number of columns away from the start of the diagonal (offset)
            t = diag[: s[0] if offset >= 0 else s[1]]
            tl_idx = t[t != "."]
            if len(tl_idx) > 0:
                adj_vals.append(tl_idx[-1])
            t = diag[s[0] + 1 if offset >= 0 else s[1] + 1 :]
            br_idx = t[t != "."]
            if len(br_idx) > 0:
                adj_vals.append(br_idx[0])

            # minor diagonal, from top right to bottom left
            flipped = np.fliplr(data)
            diag = np.diagonal(flipped, (flipped.shape[1] - 1) - s[0] - s[1])
            t = diag[: s[0] if offset >= 0 else s[1]]
            tr_idx = t[t != "."]
            if len(tr_idx) > 0:
                adj_vals.append(tr_idx[-1])
            t = diag[s[0] + 1 if offset >= 0 else s[1] + 1 :]
            bl_idx = t[t != "."]
            if len(bl_idx) > 0:
                adj_vals.append(bl_idx[0])

            cnt = 0
            print(adj_vals)
            for v in adj_vals:
                if v == "#":
                    cnt += 1

            nums[s[0], s[1]] = cnt

        print(nums)
        new_data = data.copy()

        new_data[np.logical_and(nums >= THRESH, data == "#")] = "L"
        new_data[np.logical_and(nums == 0, data == "L")] = "#"
        if np.array_equal(new_data, data):
            print(np.sum(new_data == "#"))
            return

        data = new_data
        imobj.set_data(data == "#" * 1)
        plt.pause(0.001)
        time.sleep(1)
        print(data)


main()
