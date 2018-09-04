'''
题目：旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
'''
'''
输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的原地算法。
'''
#注：nums[:]为leetcode在线判定系统，判定空间占用的方式，直接返回nums结果相同


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    nums[:] = nums[n-k:]+nums[:n-k]


print(rotate([-1,-100,3,99], 2))
