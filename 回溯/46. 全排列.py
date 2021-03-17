class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def backtrack(nums, track):
            if len(track) == len(nums):
                self.res.append(track)

            # 模板开始
            for each in nums:
                if each in track:
                    continue
                # step1.
                track.append(each)
                backtrack(nums, track)
                # step2.
                track.pop(-1)
        track = []
        backtrack(nums, track)
        return self.res