'''
题目：买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
'''
'''
示例：
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
'''
#核心：求出数组中的max与min，且max位于min后


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0:
        return 0
    ret = 0#存储当前指向值减去最小值
    curMin = prices[0]#存储数组最小值
    for i in range(0, len(prices)):
        curMin = min(curMin, prices[i])
        ret = max(ret, prices[i] - curMin)
    return ret


print(maxProfit([7, 1, 5, 3, 6, 4]))

