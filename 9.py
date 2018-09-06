'''
题目：回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
'''
'''
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
'''


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    elif int(x/10) == 0:
        return True
    res = 0
    t = x
    while t != 0:
        res = res * 10 + t % 10
        t = int(t/10)
    if x == res:
        return True
    else:
        return False

