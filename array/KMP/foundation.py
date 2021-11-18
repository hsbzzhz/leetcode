class KMP(object):
    def __init__(self, pattern: str, s: str):
        self.pattern = pattern
        self.s = s

    def prefix_table(self):
        n = len(self.pattern)
        prefix = [0] * n
        i, j = 1, 0
        while i < n:
            if self.pattern[i] == self.pattern[j]:
                j += 1
                prefix[i] = j
                i += 1
            else:
                if j > 0:
                    j = prefix[j - 1]
                else:
                    prefix[i] = j
                    i += 1
        # 移位
        temp = [-1]
        temp.extend(prefix[:-1])
        return temp

    def search(self):
        prefix_table = self.prefix_table()
        """
        pattern   raw
           j       i
           n       m
        """
        i, j = 0, 0
        m, n = len(self.s), len(self.pattern)
        while i < m:
            if j == n - 1 and self.s[i] == self.pattern[j]:
                print("found at {}".format(i - j))
                j = prefix_table[j]
                if j == prefix_table[0]:
                    i += 1
                    j += 1
                    continue
            if self.s[i] == self.pattern[j]:
                i += 1
                j += 1
            else:
                j = prefix_table[j]
                if j == prefix_table[0]:
                    i += 1
                    j += 1


demo = KMP("ababcabaa", "ababhfababcabaaababcabaa")
print(demo.prefix_table())
demo.search()
