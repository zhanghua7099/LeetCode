'''
题目：缺失数字
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
'''
'''
示例:
输入: [9,6,4,2,3,5,7,0,1]
输出: 8
说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
'''
#核心：利用数学公式，前n项和减去数组元素和，等于缺失数字


def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum = 0
    for i in nums:
        sum += i
    n = len(nums)+1
    sum1 = 0
    for t in range(n):
        sum1 += t
    return sum1 - sum


print(missingNumber([9,6,4,2,3,5,7,0,1]))
