'''
题目：计数质数
统计所有小于非负整数 n 的质数的数量。
'''
'''
示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 
'''


import math
def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 3:
        return 0
    res = [True] * n
    res[0] = res[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        res[i * i:n:i] = [False] * len(res[i * i:n:i])
    return sum(res)
