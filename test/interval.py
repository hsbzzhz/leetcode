from test.subtract import setSubtract
basetimeline = [(1,25)]
w1 = [(1,3),(5,9),(15, 17)]
w2 = [(2,4),(7,9),(13, 16),(17,19)]

#except_result:
w1_e = [(1, 3), (5, 9), (13, 17)]
w2_e = [(3, 4), (13, 15), (17,19)]
blank = [(4,5), (9, 13), (19,25)]

step1 = setSubtract(basetimeline,w1)
step2 = setSubtract(step1,w2)

print(step2)