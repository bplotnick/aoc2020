import logging
from collections import defaultdict
from typing import Dict

filename = "input.txt"


def check_pass(line: str) -> bool:
    length_req, letter, password = line.split()
    letter = letter.rstrip(":")

    left, right = length_req.split("-")
    left_count = int(left)
    right_count = int(right)

    counts: Dict[str, int] = defaultdict(int)
    for l in password:
        counts[l] += 1

    if counts[letter] >= left_count and counts[letter] <= right_count:
        return True

    return False


def main():
    num_valid = 0
    with open(filename) as f:
        for line in f:
            is_valid = check_pass(line)
            logging.debug(f"line: {line} -- {is_valid}")
            if is_valid:
                num_valid += 1
    print(num_valid)


if __name__ == "__main__":
    main()
