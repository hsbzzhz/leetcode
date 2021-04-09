class RangeSet:
    def __init__(self, elements):
        self.ranges = list(elements)

    def __iter__(self):
        return iter(self.ranges)

    def __repr__(self):
        return "RangeSet: %r" % self.ranges

    def has(self, tup):
        for pos, i in enumerate(self.ranges):
            if i[0] <= tup[0] and i[1] >= tup[1]:
                return pos, i
        raise ValueError("Invalid range or overlapping range")

    def minus(self, tup):
        pos, (x, y) = self.has(tup)
        out = []
        if x < tup[0]:
            out.append((x, tup[0] - 1))
        if y > tup[1]:
            out.append((tup[1] + 1, y))
        self.ranges[pos : pos + 1] = out

    def __sub__(self, r):
        r1 = RangeSet(self)
        for i in r:
            r1.minus(i)
        return r1

    def sub(self, r):  # inplace subtraction
        for i in r:
            self.minus(i)


def setSubtract(l1, l2):
    # l1 = condense(l1)
    # l2 = condense(l2)
    i = 0
    for t in l2:
        while t[0] > l1[i][1]:
            i += 1
            if i >= len(l1):
                break
        if t[1] < l1[i][1] and t[0] > l1[i][0]:
            # t cuts l1[i] in 2 pieces
            l1 = l1[:i] + [(l1[i][0], t[0] - 1), (t[1] + 1, l1[i][1])] + l1[i + 1 :]
        elif t[1] >= l1[i][1] and t[0] <= l1[i][0]:
            # t eliminates l1[i]
            l1.pop(i)
        elif t[1] >= l1[i][1]:
            # t cuts off the top end of l1[i]
            l1[i] = (l1[i][0], t[0] - 1)
        elif t[0] <= l1[i][0]:
            # t cuts off the bottom end of l1[i]
            l1[i] = (t[1] + 1, l1[i][1])
        else:
            print("This shouldn't happen...")
            exit()
    return l1
