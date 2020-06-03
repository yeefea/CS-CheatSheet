"""
动态规划算法分为4步
1. 描述最优解的结构
2. 递归定义最优解的值
3. 自底向上算出最优解的值
4. 用计算出的结果构造一个最优解
"""
import numpy as np

"""
把算法变简单

最简单的动态规划
爬楼梯

稍难一些
走格子

算法导论
最快流水线
矩阵连乘

备忘录

"""


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
    dp = [[0 for _ in range(y + 1)] for _ in range(x + 1)]
    for i in range(x + 1):
        dp[i][0] = 1
    for i in range(y + 1):
        dp[0][i] = 1
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[x][y]


def lowest_cost(e, a, t, x):
    """
    《算法导论》 15.1 装配线调度
    装配线i, i = 0, 1
    进入装配线所需的时间e0, e1
    离开装配线所需的时间x0, x1
    装配站加工时间ai,j
    从装配线i的第j个装配站移动到装配线另一条装配线j+1装配站所需的时间ti,j

    递归解: f* = min(f1[n] + x1, f2[n] + x2)

    改写简化下标

    S(i,j)表示装配站
    t(i,j)表示从S(i,j)移走零件需要的时间
    i = 0, 1
    j = 0, 1, ... , n

    e0, e1
    x0, x1

    c_out = min(c(0,n)+x0,c(1,n)+x1)
    c(0,j) = min(c(0,j-1), c(1,j-1)+t(1,j-1))+S(0,j)
    c(1,j) = min(c(1,j-1), c(0,j-1)+t(0,j-1))+S(1,j)

    c(0,0) = 2+7=9
    c(1,0) = 4+8=12

    :param e: [2,4]
    :param a: [[7,9,3,4,8,4],
               [8,5,6,4,5,7]]
    :param t: [[2,3,1,3,4],
               [2,1,2,2,1]]
    :param x: [3,2]
    :return:
    """
    n_station = len(a[0])
    f = []
    f.append([0] * (n_station + 1))
    f.append([0] * (n_station + 1))
    f[0][0] = e[0] + a[0][0]
    f[1][0] = e[1] + a[1][0]
    for j in range(1, n_station):
        f[0][j] = min(f[0][j - 1], f[1][j - 1] + t[1][j - 1]) + a[0][j]
        f[1][j] = min(f[1][j - 1], f[0][j - 1] + t[0][j - 1]) + a[1][j]
    f[0][-1] = f[0][-2] + x[0]
    f[1][-1] = f[1][-2] + x[1]
    return min(f[0][-1], f[1][-1])


def fastest_way(e, a, t, x):
    n_station = len(a[0])
    f = []
    f.append([0] * (n_station + 1))
    f.append([0] * (n_station + 1))
    f[0][0] = e[0] + a[0][0]
    f[1][0] = e[1] + a[1][0]
    l = []
    l.append([None] * n_station)
    l.append([None] * n_station)
    for j in range(1, n_station):
        print(j)
        c0 = f[0][j - 1]
        c1 = f[1][j - 1] + t[1][j - 1]
        if c0 <= c1:
            f[0][j] = c0 + a[0][j]
            l[0][j] = 0
        else:
            f[0][j] = c1 + a[0][j]
            l[0][j] = 1

        c0 = f[0][j - 1] + t[0][j - 1]
        c1 = f[1][j - 1]
        if c1 <= c0:
            f[1][j] = c1 + a[1][j]
            l[1][j] = 1
        else:
            f[1][j] = c0 + a[1][j]
            l[1][j] = 0

    f[0][-1] = f[0][-2] + x[0]
    f[1][-1] = f[1][-2] + x[1]
    if f[0][-1] <= f[1][-1]:
        f_star = f[0][-1]
        l_star = 0
    else:
        f_star = f[1][-1]
        l_star = 1
    i = l_star  # 0
    print_line_recursive(l, i, len(l[0]) - 1)
    # for j in range(len(l[0]) - 1, 0, -1):
    #     i = l[i][j]
    #     print('line', l[i][j], 'station', j)
    print('output', 'line', l_star)


def print_line_recursive(lines, line_n, station_n):
    if station_n == 1:
        line = lines[line_n][station_n]
        print('station', station_n, 'line', line)
        return
    line = lines[line_n][station_n]
    print_line_recursive(lines, line, station_n - 1)
    print('station', station_n, 'line', line)


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
    return recursion_2d(x - 1, y) + recursion_2d(x, y - 1)


if __name__ == '__main__':
    # 测试动态规划解流水线问题
    e = [2, 4]
    a = [[7, 9, 3, 4, 8, 4],
         [8, 5, 6, 4, 5, 7]]
    t = [[2, 3, 1, 3, 4],
         [2, 1, 2, 2, 1]]
    x = [3, 2]
    fastest_way(e, a, t, x)

    # 测试递归解爬楼梯问题
    print(climbing_steps_recursive(10))

    # 测试动态规划解爬楼梯问题
    print(climbing_steps(10))

    # 测试动态规划解0/1背包问题
    res = knapsack_problem_01(5, np.array([3, 4, 5]), np.array([4, 5, 6]))
    print(res)
    print(dynamic_programming_2d(3, 5))
