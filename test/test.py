import itertools


def range_diff(r1, r2):
    s1, e1 = r1
    s2, e2 = r2
    endpoints = sorted((s1, s2, e1, e2))
    result = []
    if endpoints[0] == s1:
        result.append((endpoints[0], endpoints[1]))
    if endpoints[3] == e1:
        result.append((endpoints[2], endpoints[3]))
    return result


def multirange_diff(r1_list, r2_list):
    for r2 in r2_list:
        r1_list = list(itertools.chain(*[range_diff(r1, r2) for r1 in r1_list]))
        result = [each for each in r1_list if each[0] != each[1]]
    return result


basetimeline = [(1, 25)]
w1 = [(1, 3), (5, 9), (15, 17)]
w2 = [(2, 4), (7, 9), (13, 16), (17, 19)]


# a = range_diff(basetimeline, w1)
step1 = multirange_diff(basetimeline, w1)
step2 = multirange_diff(step1, w2)
print(step2)
