import numpy as np
from itertools import groupby

# I mean ... there's probably some math here with binomial coefficients or something...
# But lookup tables work, man!
lookuptable = {
    1: 1,
    2: 2,
    3: 4,
    4: 7,
}


def main():
    data = np.loadtxt("input.txt", dtype=int)

    data = np.append(data, [0, data.max() + 3])
    data.sort()
    # 1st discrete difference determines "distance" of elements
    diff = np.diff(data)

    # Run-length encoding of the diff, but only the 1's. We can't reduce 3's.
    rle = [len(list(v)) for k, v in groupby(diff) if k == 1]

    total = 1
    # The lookup table determines the number of ways a run of numbers (with difference 1) can be "collapsed"
    # Multiply them all to get the total number of combinations
    for i in rle:
        total *= lookuptable[i]
    print(total)


main()
