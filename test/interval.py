import itertools

basetimeline = [(1, 25)]
w1 = [(1, 3), (5, 9), (15, 17)]
w2 = [(2, 4), (7, 9), (13, 16), (17, 19)]


####
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


# except_result:
w1_e = [(1, 3), (5, 9), (13, 17)]
w2_e = [(3, 4), (13, 15), (17, 19)]
blank = [(4, 5), (9, 13), (19, 25)]

step1 = setSubtract(basetimeline, w1)
step2 = setSubtract(step1, w2)

print(step1)
