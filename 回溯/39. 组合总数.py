"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        """
        做减法
        :param candidates:
        :param target:
        :return:
        """
        res = list()
        candidates.sort()
        def backtrace(candidates:[] ,path: [int], start: int, target: int):
            """

            :param candidates:
            :param start:
            :param target: 每次递归，做完减法后还剩下的
            :return:
            """
            # 跳出递归
            if target == 0:
                res.append(path[:])
                return
            # 如果是range(len(candidates)), 就会出现重复解,加上start 就不会
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    path.append(candidates[i])
                    backtrace(candidates, path, i, target - candidates[i])
                    path.pop(-1)
        backtrace(candidates, [], 0, target)
        return res

s = Solution()
nums = [2, 3, 6, 7]
target = 7
res = s.combinationSum(nums, target)

print(res)
