from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]] = 1
            else:
                hash_table[nums[i]] += 1
        after = dict(sorted(hash_table.items(), key=lambda item:item[1], reverse=True))
        res = []
        for ke,v in after.items():
            if k <= 0:
                break
            res.append(ke)
            k -= 1
        return res

demo = Solution()
res = demo.topKFrequent([3, 0, 1, 0], 1)
print(res)