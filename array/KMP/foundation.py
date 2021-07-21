class KMP(object):
    def __init__(self, pattern: str, s: str):
        self.pattern= pattern
        self.s = s

    def prefix_table(self):
        n = len(self.pattern)
        prefix = [0]*n
        i, j = 1, 0
        while i < n:
            if self.pattern[i] == self.pattern[j]:
                j += 1
                prefix[i] = j
                i += 1
            else:
                if j>0:
                    j = prefix[j - 1]
                else:
                    prefix[i] = j
                    i+=1
        return prefix



demo = KMP('ababc', 'dfghhhhf')
print(demo.prefix_table())