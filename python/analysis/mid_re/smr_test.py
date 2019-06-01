# coding: utf-8
#
# smirnov_grubbs(data, alpha)
#   Generate outlier-removed data with Smirnov-Grubbs.
#
#   Parameters:
#     data: array_like
#       Numeric data values.
#     alpha: float
#       Significance level. (two-sided)
#
#   Returns:
#     outlier-removed-data
#     outlier-data
#
#   e.g.
#     data = [1, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 1000]
#     alpha = 0.01
#     smirnov_grubbs(data, alpha)
#     ==> ([100, 101, 102, 103, 104, 105, 106, 107, 108, 109], [1000, 1])

import numpy as np
import scipy.stats as stats

def smirnov_grubbs(data, alpha):
    x, o = list(data), []
    xi, oi = [ i for i in range(len(x))], []
    while True:
        n = len(x)
        t = stats.t.isf(q=(alpha / n) / 2, df=n - 2)
        tau = (n - 1) * t / np.sqrt(n * (n - 2) + n * t * t)
        i_min, i_max = np.argmin(x), np.argmax(x)
        myu, std = np.mean(x), np.std(x, ddof=1)
        i_far = i_max if np.abs(x[i_max] - myu) > np.abs(x[i_min] - myu) else i_min
        tau_far = np.abs((x[i_far] - myu) / std)
        if tau_far < tau: break
        o.append(x.pop(i_far))
        oi.append(xi.pop(i_far))
    return (np.array(x), np.array(o), xi, oi)