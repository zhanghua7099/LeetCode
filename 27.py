'''
题目：移除元素
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
'''
'''
示例：
输入：nums = [0,1,2,2,3,0,4,2], val = 2,
输出：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
'''


def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    index = 0
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index = index + 1
    return index


print(removeElement([0,1,2,2,3,0,4,2], 2))
