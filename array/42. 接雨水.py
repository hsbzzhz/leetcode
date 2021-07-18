from typing import List
"""
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
https://leetcode-cn.com/problems/trapping-rain-water/
"""

class Solution:
    def trap0(self, height: List[int]) -> int:
        """
        todo bug fix
        :param height:
        :return:
        """
        max_index = height.index(max(height))
        res = 0
        for left in range(0, max_index):
            for i in range(left+1, max_index):
                if height[i] < height[left]:
                    res += height[left] - height[i]
                else:
                    left = i

        for right in range(len(height)-1, max_index, -1):
            for j in range(right-1, max_index, -1):
                if height[j] < height[right]:
                    res += height[right] - height[j]
                else:
                    right = j
        return res

    def trap1(self, height: List[int]) -> int:
        """
        暴力法 O(n^2)
        :param height:
        :return:
        """
        ans = 0
        for i in range(1, len(height)-1):
            max_left, max_right = 0, 0
            # 寻找左边最高
            left, right = i, i
            while left >= 0:
                max_left = max(max_left, height[left])
                left -= 1
            # 寻找右边最高
            while right < len(height):
                max_right = max(max_right, height[right])
                right += 1
            ans += min(max_right, max_left) - height[i]
        return ans

    def trap2(self, height: List[int]) -> int:
        """
        双指针 O(n)
        :param height:
        :return:
        """
        left, left_max = 0, 0
        right, right_max = len(height)-1, 0
        sum = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                sum = sum + left_max - height[left]
                left += 1
            else:
                sum = sum + right_max - height[right]
                right -= 1
        return sum


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
demo = Solution()
output = demo.trap2(height)
print(output)