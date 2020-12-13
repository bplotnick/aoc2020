import numpy as np
from scipy.signal import convolve2d
import matplotlib

matplotlib.use("macosx")
import matplotlib.pyplot as plt
import time

adjacency_kernel = np.ones((3, 3), dtype=int)
THRESH = 5  # Threshold is 4 but the cell itself is set to 1 so we add one


def main():
    data = np.loadtxt(
        "input.txt", dtype="str", converters={0: lambda x: list(x.decode("utf-8"))}
    )
    floor_cells = data == "."

    nums = np.zeros_like(data, dtype=bool)
    nums[data == "#"] = True
    plt.ion()
    imobj = plt.matshow(nums * 1, vmin=0, vmax=1)
    plt.pause(0.001)
    while True:
        new_nums = np.copy(nums)
        conv = convolve2d(nums, adjacency_kernel, mode="same")

        new_nums[np.logical_and(conv >= THRESH, nums == True)] = False
        new_nums[np.logical_and(conv == 0, nums == False)] = True
        new_nums[floor_cells] = False
        if np.array_equal(new_nums, nums):
            print(np.sum(nums))
            return

        nums = new_nums
        imobj.set_data(nums * 1)
        plt.pause(0.001)
        #        time.sleep(1)
        print(nums)


main()
