import logging
from collections import defaultdict
filename = 'input.txt'

def check_pass(line: str) -> bool:
    length_req, letter, password = line.split()
    letter = letter.rstrip(':')

    left, right = length_req.split('-')
    left = int(left) - 1
    right = int(right) - 1

    if ((password[left] == letter) ^ (password[right] == letter)):
        return True

    return False

def main():
    num_valid = 0
    with open(filename) as f:
        for line in f:
            is_valid = check_pass(line)
            logging.debug(f'line: {line} -- {is_valid}')
            if is_valid:
                num_valid += 1
    print(num_valid)

if __name__ == '__main__':
    main()
