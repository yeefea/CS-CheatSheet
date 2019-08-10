"""
幻方
"""


def _new_empty_square(degree: int):
    return [[None] * degree for _ in range(degree)]


def get_odd_magic_square(degree: int):
    """
    奇数阶幻方
    :param degree:
    :return:
    """
    if degree < 3:
        raise ValueError('invalid degree')
    if degree % 2 == 0:
        raise ValueError('invalid degree')
    nums = list(range(1, 1 + degree * degree))
    magic_square = _new_empty_square(degree)
    i = 0
    j = degree // 2
    for n in nums:
        magic_square[i][j] = n
        tmp_i = (i - 1) % degree
        tmp_j = (j + 1) % degree
        if magic_square[tmp_i][tmp_j] is None:
            i = tmp_i
            j = tmp_j
        else:
            i = (i + 1) % degree
    return magic_square


print(get_odd_magic_square(3))
