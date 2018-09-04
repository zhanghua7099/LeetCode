'''
题目：求众数
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数。
'''
'''
示例:
输入: [2,2,1,1,1,2,2]
输出: 2
'''
#核心:利用哈希表，从左到右依次遍历存入字典，并。键为当前数组值，值为数组值出现次数，当出现次数大于n/2时返回键。


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i]=1
        else:
            dic[i] += 1
        if dic[i] >= len(nums)/2:
            return i


print(majorityElement([3,2,3]))
