'''
题目：爬楼梯
假设你正在爬楼梯。需要 n 步你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
'''
'''
示例：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
    1.  1 步 + 1 步 + 1 步
    2.  1 步 + 2 步
    3.  2 步 + 1 步
'''


def climbStairs(n):
    """
    动态规划爬楼梯
    dp[i]=dp[i-1]+dp[i-2],初始条件dp[1]=1, dp[2]=2
    :type n: int
    :rtype: int
    """
    t1 = 1
    t2 = 2
    climbsum = t1+t2
    for i in range(n-3):
        t1 = t2
        t2 = climbsum
        climbsum = climbsum + t1
    return climbsum


print(climbStairs(3))
