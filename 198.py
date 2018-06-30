'''
题目：打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
'''
'''
示例：
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
'''


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) > 2:
        numSum = []
        MaxSum = 0
        numSum.append(nums[0])
        if nums[0] > nums[1]:
            numSum.append(nums[0])
        else:
            numSum.append(nums[1])
        for i in range(2, len(nums)):
            numSum.append(max(numSum[i - 2] + nums[i], numSum[i - 1]))
        for t in numSum:
            if t >= MaxSum:
                MaxSum = t
        return MaxSum
    elif len(nums) == 2:
        if nums[0] > nums[1]:
            return nums[0]
        else:
            return nums[1]
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 0:
        return 0


print(rob([2,7,9,3,1]))
