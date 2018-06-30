'''
题目：加一
给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
示例：
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
'''
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    s = 0
    for i in digits:
        s = s*10 + i
    s = str(s+1)
    lst = []
    for t in s:
        lst.append(int(t))
    return lst


print(plusOne([1,2,3]))
