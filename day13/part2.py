import math


def main():
    with open("input.txt") as f:
        f.readline()
        busses = f.readline().split(",")
    busses = [(idx, int(v.strip())) for idx, v in enumerate(busses) if v != "x"]
    maxbus = max(busses, key=lambda x: x[1])
    print(maxbus)
    """
    maxval = 0
    maxidx = 0
    for b in range(len(busses)):
        curbus = busses[b]
        curval = curbus[1]
        curidx = curbus[0]
        if curval > maxval:
            maxval = curval
            maxidx = curidx
    """
    for b in range(len(busses)):
        curbus = busses[b]
        busses[b] = (curbus[0] - maxbus[0], curbus[1])
    print(busses)
    val = maxbus[1]
    x = 1
    while True:
        tmp = val * x
        found = True
        for b in busses:
            if (tmp + b[0]) % b[1] != 0:
                found = False
                break

        if found is True:
            print(x)
            print(tmp + busses[0][0])
            break

        if x % 1000000 == 0:
            print(x, tmp)
        x += 1


main()
