def basel_problem(n_iter):
    """
    :param n_iter:迭代次数
    :return:
    """
    res = 0.0
    for i in range(1, n_iter + 1):
        res += 1.0 / (i * i)
    return res


if __name__ == '__main__':
    print(basel_problem(100000))