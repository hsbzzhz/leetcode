"""
给定一个无重复元素的数组 candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。

candidates中的数字可以无限制重复被选取。

说明：

所有数字（包括target）都是正整数。
解集不能包含重复的组合。
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

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
        传入 target 做减法
        :param candidates:
        :param target:
        :return:
        """
        res = list()
        candidates.sort()

        def backtrace(candidates: [], path: [int], start: int, target: int):
            """

            :param candidates: 选择列表
            :param start: 记录位置指针，选择列表从 start 往后
            :param target: 每次递归，做减法
            :return:
            """
            # 跳出递归
            if target == 0:
                res.append(path[:])
                return
            # 如果是 range(len(candidates)), 就会出现重复解
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    path.append(candidates[i])
                    #
                    backtrace(candidates, path, i, target - candidates[i])
                    path.pop(-1)

        backtrace(candidates, [], 0, target)
        return res


s = Solution()
nums = [2, 3, 6, 7]
target = 7
res = s.combinationSum(nums, target)

print(res)
