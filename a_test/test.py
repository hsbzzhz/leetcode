from typing import List

test1 = [100, 4, 200, 1, 3, 2]

def longestConsecutive(nums: List[int]) -> int:
    max_length = 0
    nums_set = set(nums)
    for each in nums_set:
        if each - 1 in nums_set:
            continue
        else:
            len = 0
            while max(nums_set) >= each and each in nums_set:
                each += 1
                len += 1
            max_length = max(len, max_length)
    return max_length