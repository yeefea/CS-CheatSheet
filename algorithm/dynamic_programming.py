"""
动态规划算法分为4步
1. 描述最优解的结构
2. 递归定义最优解的值
3. 自底向上算出最优解的值
4. 用计算出的结果构造一个最优解
"""
import numpy as np


def fastest_way(e, a, t, x):
    """
    《算法导论》 15.1 装配线调度
    装配线i, i = 0, 1
    进入装配线所需的时间e0, e1
    离开装配线所需的时间x0, x1
    装配站加工时间ai,j
    从装配线i的第j个装配站移动到装配线另一条装配线j+1装配站所需的时间ti,j

    递归解: f* = min(f1[n] + x1, f2[n] + x2)
    :param e: [2,4]
    :param a: [[7,9,3,4,8,4],
               [8,5,6,4,5,7]]
    :param t: [[2,3,1,3,4],
               [2,1,2,2,1]]
    :param x: [3,2]
    :return:
    """
    len_array = a.shape[1]
    f = np.zeros((2, len_array))
    l = np.zeros((2, len_array))
    f[0, 0] = e[0] + a[0, 0]  # 通过l0第0个装配线所需时间
    f[1, 0] = e[1] + a[1, 0]  # 通过l1第0个装配线所需时间
    l[0, 0] = 0
    l[1, 0] = 1
    for j in range(1, len_array):
        cost_l0_to_l0 = f[0, j - 1] + a[0, j]
        cost_l1_to_l0 = f[1, j - 1] + t[1, j - 1] + a[0, j]
        if cost_l0_to_l0 <= cost_l1_to_l0:  # l0 -> l0 比 l1 -> l0更快
            f[0, j] = cost_l0_to_l0
            l[0, j] = 0
        else:
            f[0, j] = cost_l1_to_l0
            l[0, j] = 1

        cost_l1_to_l1 = f[1, j - 1] + a[1, j]
        cost_l0_to_l1 = f[0, j - 1] + t[0, j - 1] + a[1, j]
        if cost_l1_to_l1 <= cost_l0_to_l1:  # l1 -> l1 比 l0 -> l1更快
            f[1, j] = cost_l1_to_l1
            l[1, j] = 1
        else:
            f[1, j] = cost_l0_to_l1
            l[1, j] = 0
    l0_out = f[0, -1] + x[0]
    l1_out = f[1, -1] + x[1]
    if l0_out <= l1_out:
        f = l0_out
        # l_out = 0
    else:
        f = l1_out
        # l_out = 1
    return f


def climbing_steps(n):
    """
    爬楼梯问题
    :param n: int 楼梯级数
    :return: 可能的走法数量
    """
    if 2 > n:
        return 1
    if 2 == n:
        return 2
    f1 = 1
    f2 = 2
    res = 0
    for i in range(2, n):
        res = f1 + f2
        f1 = f2
        f2 = res
    return res


def climbing_steps_recursive(n):
    if 2 > n:
        return 1
    if 2 == n:
        return 2
    return climbing_steps_recursive(n - 1) + climbing_steps_recursive(n - 2)


def knapsack_problem_01(max_weight, w, v):
    """

    :param max_weight: 背包可以放入的最大重量
    :param w: 物品重量 [3,4,5]
    :param v: 物品价值 [4,5,6]
    :return:
    """
    cache = np.zeros((w.shape[0] + 1, max_weight + 1))
    for i in range(1, cache.shape[0]):
        for j in range(1, cache.shape[1]):
            if w[i - 1] <= j:
                v_add_item = cache[i - 1, j - w[i - 1]] + v[i - 1]  # 加入物品
                v_not_add_item = cache[i - 1, j]  # 不加物品
                if v_add_item >= v_not_add_item:
                    cache[i, j] = v_add_item
                else:
                    cache[i, j] = v_not_add_item
            else:
                cache[i, j] = cache[i - 1, j]
    return cache[-1, -1]


def recursion_2d(x, y):
    if x == 0 and y == 0:
        return 0
    if x == 0 or y == 0:
        return 1
    x, y = abs(x), abs(y)
    return recursion_2d(x-1, y) + recursion_2d(x, y-1)


def dynamic_programming_2d(x, y):
    """
    dp[i][0] = 1 for i = 0,...,x
    dp[0][j] = 1 for j = 0,...,y
    dp[x][y] = dp[x-1][y] + dp[x][y-1]
    """
    if x == 0 and y == 0:
        return 0
    if x == 0 or y == 0:
        return 1
    x, y = abs(x), abs(y)
    dp = [[0 for _ in range(y+1)] for _ in range(x+1)]
    for i in range(x+1):
        dp[i][0] = 1
    for i in range(y+1):
        dp[0][i] = 1
    for i in range(1, x+1):
        for j in range(1, y+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[x][y]


if __name__ == '__main__':
    # 测试动态规划解流水线问题
    e = np.array([2, 4])
    a = np.array([[7, 9, 3, 4, 8, 4],
                  [8, 5, 6, 4, 5, 7]])
    t = np.array([[2, 3, 1, 3, 4],
                  [2, 1, 2, 2, 1]])
    x = np.array([3, 2])
    print(fastest_way(e, a, t, x))

    # 测试递归解爬楼梯问题
    print(climbing_steps_recursive(10))

    # 测试动态规划解爬楼梯问题
    print(climbing_steps(10))

    # 测试动态规划解0/1背包问题
    res = knapsack_problem_01(5, np.array([3, 4, 5]), np.array([4, 5, 6]))
    print(res)
    print(dynamic_programming_2d(3, 5))