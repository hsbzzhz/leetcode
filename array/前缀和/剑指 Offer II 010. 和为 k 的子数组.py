class Solution:
    """
    给定一个整数数组和一个整数k ，请找到该数组中和为k的连续子数组的个数。

    示例 1 :

    输入:nums = [1,1,1], k = 2
    输出: 2
    解释: 此题 [1,1] 与 [1,1] 为两种不同的情况
    示例 2
    输入:nums = [1,2,3], k = 3
    输出: 2

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/QTMn0o
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        # key：前缀和，val：对应的数量
        pre_sum_map = {0: 1}  # 初始化，前缀和为 0 的个数为 1

        pre_sum = 0  # 记录自首个元素累计的前缀和
        count = 0

        for num in nums:  # 遍历所有元素：计算前缀和，寻找 k，更新 map
            pre_sum += num  # 累计前缀和

            # 根据 pre - (pre - k) = k，寻找连续数组为 pre - k 的数量，即连续数组的和为 k 的数量
            # 说明：pre 为自首个元素开始累计的连续数组；
            # pre - k 为包含在连续数组 pre 中的一个连续子数组（自首个元素开始累计）
            # 连续数组 - 连续子数组 = 连续子数组，对应 pre - (pre - k) = k
            # 则连续数组的和为 pre - k 的数量，即为连续数组的和为 k 的数量
            if pre_sum - k in pre_sum_map:    # 这一节要写在初始化map前面，不然跑不通 【1】0 的case
                count += pre_sum_map[pre_sum - k]

            if pre_sum in pre_sum_map:  # 此时的前缀和被记录过，则在原始记录上 + 1
                pre_sum_map[pre_sum] += 1
            else:  # 如果此时的前缀和没有出现过，则初始化为 1
                pre_sum_map[pre_sum] = 1

        return count