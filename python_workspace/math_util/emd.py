import numpy as np

from scipy.signal import argrelextrema, argrelmax, argrelmin
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt


def emd(arr: np.ndarray):
    x = np.arange(arr.size)
    maxima = argrelmax(arr)
    minima = argrelmin(arr)
    cs_max = CubicSpline(maxima[0], arr[maxima[0]])
    cs_min = CubicSpline(minima[0], arr[minima[0]])
    xs = np.arange(0, arr.size, 1)
    cs_mean = 0.5 * (cs_max(xs) + cs_min(xs))
    fig, ax = plt.subplots()
    ax.plot(x, arr, label='data')
    ax.plot(xs, cs_max(xs), label='maximum')
    ax.plot(xs, cs_min(xs), label='minimum')
    ax.plot(xs, cs_mean, label='mean')
    ax.legend()
    plt.show()
    fig, ax = plt.subplots()
    ax.plot(xs, arr - cs_mean, label='residual')
    plt.show()

    # print(maxima, arr[maxima[0]])
    # print(minima, arr[minima[0]])


def wiener_process(t, a, b):
    x0 = 0
    dx = a + b * np.random.standard_normal(t)
    res = np.zeros(t + 1)
    x_last = x0
    for i in range(t):
        tmp = dx[i] + x_last
        res[i + 1] = tmp
        x_last = tmp
    return res


TRADE_DAYS_PER_YEAR = 365


def stock_price_model(s0, n_days, expect_return, volatility):
    """

    年化预期收益率
    年化波动率
    """
    day = 1.0 / TRADE_DAYS_PER_YEAR
    res = np.zeros(n_days + 1)
    res[0] = s0
    ds = expect_return * day + volatility * np.sqrt(day) * np.random.standard_normal(n_days)
    for i in range(n_days):
        tmp = res[i] * (1.0 + ds[i])
        res[i + 1] = tmp
    return res


if __name__ == '__main__':
    emd(stock_price_model(100.0, TRADE_DAYS_PER_YEAR, 0.15, 0.3))
