'''
题目：删除排序数组中的重复项
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
'''
'''
示例：
输入：nums = [0,0,1,1,1,2,2,3,3,4],
输出：函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。
'''


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    index = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[index]:
            index = index + 1
            nums[index] = nums[i]
    return index + 1


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
