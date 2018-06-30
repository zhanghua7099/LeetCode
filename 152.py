'''
题目：乘积最大子序列
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
'''
'''
示例：
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
'''


def maxProduct(nums):
    """
    动态规划求最大子乘积和
    maxend = max(max(maxend*data[i] , minend*data[i]) , data[i]);
    minend = min(min(maxend*data[i] , minend*data[i]) , data[i]);
    :type nums: List[int]
    :rtype: int
    """
    Max = nums[0]
    MaxEnd = []
    MinEnd = []
    MaxEnd.append(nums[0])
    MinEnd.append(nums[0])
    for i in range(1, len(nums)):
        MaxEnd.append(max(MaxEnd[i-1]*nums[i], MinEnd[i-1]*nums[i], nums[i]))
        MinEnd.append(min(MaxEnd[i-1]*nums[i], MinEnd[i-1]*nums[i], nums[i]))
    for i in MaxEnd:
        if i >= Max:
            Max = i
    return Max


print(maxProduct([2,3,-2,4]))
