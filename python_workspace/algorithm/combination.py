"""
组合

1 2 3 4, k=3

123
124
134
234
"""


def combination(elements, k):
    if k < 0:
        raise ValueError(k)
    if k == 0:
        return []
    res = []
    k -= 1
    for i in range(len(elements)):
        if k == 0:
            res.append([elements[i]])
            continue
        tmp = combination(elements[i + 1:], k)
        for x in tmp:
            res.append([elements[i]] + x)
    return res


print(combination('1234', 2))
