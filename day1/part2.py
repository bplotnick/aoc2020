from typing import List

FILENAME = 'input.txt'

def read_file(path: str) -> List[int]:
    with open(path) as f:            
        i = [int(i) for i in f]
    return sorted(i)

def find_nums(nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1
    while l + 1 < r:
        c = l + 1
        numsum = nums[l] + nums[c] + nums[r]
        while c < r:
            numsum = nums[l] + nums[c] + nums[r]
            if (numsum == 2020):
                print(f"Found: {nums[l]}, {nums[c]}, and {nums[r]} at indexes {l}, {c}, and {r}")
                return nums[l] * nums[c] * nums[r]
            else:
                c += 1
        if (numsum > 2020):
            r -= 1
        else:
            l +=1
            

def main():
    nums = read_file(FILENAME)
    print(find_nums(nums))
    
if __name__ == '__main__':
    main()
