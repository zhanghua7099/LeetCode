'''
题目：存在重复元素
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
'''
'''
示例 :
输入: [1,2,3,1]
输出: true
'''


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
        if dic[i] > 1:
            return True
    return False


print(containsDuplicate([1,2,3,1]))