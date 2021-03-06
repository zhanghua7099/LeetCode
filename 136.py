'''
题目：只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
'''
'''
示例 1:
输入: [2,2,1]
输出: 1
'''
#核心：利用数字的异或操作，异或操作同0异1.假设数组元素1，2，1，3，3，则异或时仅剩下2，因为3，3与1，1均为0，0与2异或为2.


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(1, len(nums)):
        nums[0] = nums[0]^nums[i]
    return nums[0]
