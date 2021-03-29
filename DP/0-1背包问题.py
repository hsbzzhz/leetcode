"""
0/1 背包问题
"""


def backpack(itemWeight, currentWeight):
    table = []
    row = col = 0
    itemValue = 0
    if itemWeight > currentWeight:
        table[row][col] = table[row-1][col]
    else:
        table[row][col] = max(table[row - 1][col], table[row-1][currentWeight - itemWeight] + itemValue)




















