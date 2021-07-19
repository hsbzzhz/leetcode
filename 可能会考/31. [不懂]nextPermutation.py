class Solution(object):
    """
    脑筋急转弯
    下一个排列
    1 4 3 2 0
    2 0 1 3 4

    下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

    如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

    必须 原地 修改，只允许使用额外常数空间。

    dfs

    示例 1：

    输入：nums = [1,2,3]
    输出：[1,3,2]
    示例 2：

    输入：nums = [3,2,1]
    输出：[1,2,3]


    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/next-permutation
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def nextPermutation(self, nums):
        """
        1. 先找出最大的索引 k 满足 nums[k] < nums[k+1]，如果不存在，就翻转整个数组；
        2. 再找出另一个最大索引 l 满足 nums[l] > nums[k]；
        3. 交换 nums[l] 和 nums[k]；
        4. 最后翻转 nums[k+1:]。
        举个例子：

        比如 nums = [1,2,7,4,3,1]，下一个排列是什么？

        我们找到第一个最大索引是 nums[1] = 2

        再找到第二个最大索引是 nums[4] = 3

        交换，nums = [1,3,7,4,2,1];

        翻转，nums = [1,3,1,2,4,7]

        完毕!

        作者：powcai
        链接：https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-powcai/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        targert_index = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                targert_index = i
                break
        nums[targert_index + 1 :].sort()
        for i in range(targert_index + 1, len(nums)):
            if nums[targert_index] < nums[i]:
                nums[targert_index], nums[i] = nums[i], nums[targert_index]
        return nums


nums = [1, 2, 3, 8, 5, 7, 6, 4]
# demo = Solution()
# res = demo.nextPermutation(nums)
# print(res)
# for i in range(len(nums)-2, -1, -1):
#     # print(nums[i])
#     if nums[i] < nums[i + 1]:
#         print(i)
#         # targert_index = len(nums) - i + 1
#         # print(targert_index)

print(nums[:5])
