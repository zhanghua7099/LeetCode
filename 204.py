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

#高效方法，核心：初始化一个全为false的列表，依次将2的倍数，3的倍数等置为true，然后返回true的个数
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


print(countPrimes(4))


class Solution:
    #自制低效版
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        sum = 0
        for i in range(2, n):
            if Solution.isPrime(i):
                sum += 1
        return sum

    @staticmethod
    def isPrime(n):
        # 判断一个数是否为素数
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True




