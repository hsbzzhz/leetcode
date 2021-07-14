from typing import List


class solution:
    """
    非 typical 回溯，太tricky 搞死人
    """
    def grayCode(self, n: int) -> List[int]:
        nums = [0, 1]
        output = []

        def dfs(arr, combin, target, idx):
            if len(combin) == target:
                output.append(int("".join([str(g) for g in combin[:]]), 2))
                return
            if idx == 0:
                for i in range(len(arr)):
                    combin.append(arr[i])
                    dfs(arr, combin, target, i)
                    combin.pop()
            if idx == 1:
                for i in range(len(arr)):
                    combin.append(arr[::-1][i])
                    dfs(arr, combin, target, i)
                    combin.pop()

        dfs(nums, [], n, 0)
        return output

