starting = [13, 16, 0, 12, 15, 1]
# starting = [1,3,2]

stop_idx = 30000000


def main():
    idx = len(starting)
    num_dict = {v: i for i, v in enumerate(starting[:-1])}
    last_num = starting[-1]

    while idx < stop_idx:
        last_seen = num_dict.get(last_num, idx - 1)
        val = (idx - 1) - last_seen
        num_dict[last_num] = idx - 1
        idx += 1
        last_num = val

    print(last_num)


main()
