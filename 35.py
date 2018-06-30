'''
题目：搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
'''
'''
示例：
输入：[1,3,5,6], 7
输出：4
'''


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int((right - left) / 2) + left
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left


print(searchInsert([1,3,5,6], 7))
