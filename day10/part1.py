import numpy as np


def main():
    data = np.loadtxt("input.txt", dtype=int)

    data = np.append(data, [0, data.max() + 3])
    data.sort()
    diff = np.diff(data)
    v, c = np.unique(diff, return_counts=True)
    soln = dict(zip(v, c))
    print(soln[1] * soln[3])


main()
