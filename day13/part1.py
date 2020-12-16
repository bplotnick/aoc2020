import math


def main():
    with open("input.txt") as f:
        ttd = int(f.readline())
        busses = f.readline().split(",")
    busses = [int(b) for b in busses if b != "x"]
    times = {}
    for b in busses:
        diff = (math.ceil(ttd / b) * b) - ttd
        times[b] = diff
    print(times)
    minbus = min(times, key=times.get)
    print(minbus)
    print(minbus * times[minbus])


main()

# 2 = math.ceil(x/13)*13 - x
