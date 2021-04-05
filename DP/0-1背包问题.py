"""
0/1 背包问题
"""


def backpack(itemWeight, currentWeight):
    """
    table[row][col] = 对于背包容积为row的时候，第 col 个物品，最后的价值
    :param itemWeight:
    :param currentWeight:
    :return:
    """
    table = []
    row = col = 0
    itemValue = 0
    if itemWeight > currentWeight:
        # 背包容量不够了，不能装入背包
        table[row][col] = table[row-1][col]
    else:
        # 选择装入背包或者不装入
        table[row][col] = max(table[row - 1][col], table[row-1][currentWeight - itemWeight] + itemValue)




















