'''
题目：存在重复元素 II
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。
'''
'''
示例:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false
'''


def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    dic = {}
    for i, num in enumerate(nums):
        if num not in dic:
            dic[num] = i
        else:
            if i - dic[num] <= k:
                return True
            else:
                dic[num] = i
    return False


print(containsNearbyDuplicate([1,2,3,1,2,3], 2))
