'''
题目：反转整数
给定一个 32 位有符号整数，将整数中的数字进行反转。
'''
'''
示例:
输入: -123
输出: -321
注意:
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
'''
#注意判定边界[−2^31,  2^31 − 1]


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    res = 0
    if x < 0:
        x = abs(x)
        while x != 0:
            res = res * 10 + x % 10
            x = int(x/10)
        if res <= 2**31:
            return -res
        else:
            return 0
    else:
        while x != 0:
            res = res * 10 + x % 10
            x = int(x/10)
        if res <= 2**31-1:
            return res
        else:
            return 0

print(reverse(-123))
