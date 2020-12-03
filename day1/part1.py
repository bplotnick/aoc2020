from typing import List
from typing import Optional

FILENAME = "input.txt"


def read_file(path: str) -> List[int]:
    with open(path) as f:
        i = [int(i) for i in f]
    return sorted(i)


def find_nums(nums: List[int]) -> Optional[int]:
    l = 0
    r = len(nums) - 1
    while l < r:
        numsum = nums[l] + nums[r]
        if numsum == 2020:
            print(f"Found: {nums[l]} and {nums[r]} at indexes {l} and {r}")
            return nums[l] * nums[r]
        elif numsum > 2020:
            r -= 1
        else:
            l += 1
    return None


def main():
    nums = read_file(FILENAME)
    print(find_nums(nums))


if __name__ == "__main__":
    main()
