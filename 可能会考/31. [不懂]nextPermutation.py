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
        从后往前找，找到第一个下降的位置，记为 k。注意k 以后的位置是降序的。 在样例中就是找到 3

        从 k 往后找，找到最小的比 k 要大的数。 找到 4

        将两者交换。注意此时 k 以后的位置仍然是降序的。

        直接将 k 以后的部分翻转（变为升序）。

        作者：AC_OIer
        链接：https://leetcode-cn.com/problems/next-permutation/solution/miao-dong-xi-lie-100-cong-xia-yi-ge-pai-gog8j/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return None

        i = len(nums) - 2
        while i >= 0 & nums[i] >= nums[i + 1]:
            # 找到第一个非生序的相邻数
            i -= 1
        if i < 0:
            nums = nums[::-1]
