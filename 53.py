'''
题目：最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
'''
'''
示例：
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''
def maxSubArray(nums):
    """
    动态规划求最大子列和
    F[i]=max{F[i-1]+a[i], a[i]}
    :type nums: List[int]
    :rtype: int
    """
    Max = nums[0]
    ThisSum = []
    ThisSum.append(nums[0])
    for i in range(1, len(nums)):
        if ThisSum[i-1]+nums[i] > nums[i]:
            ThisSum.append(ThisSum[i-1]+nums[i])
        else:
            ThisSum.append(nums[i])
    for i in ThisSum:
        if i >= Max:
            Max = i
    return Max
