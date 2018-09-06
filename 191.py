'''
题目：位1的个数
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
'''
'''
示例 2:
输入: 128
输出: 1
解释: 整数 128 的二进制表示为 00000000000000000000000010000000
'''


def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    sum = 0
    while n != 0:
        res = n % 2
        if res == 1:
            sum += 1
        n = int(n / 2)
    return sum

print(hammingWeight(11))
