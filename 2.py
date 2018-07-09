'''
题目：
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。
'''
'''
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        temp = ans
        tempsum = 0
        while True:
            if (l1 != None):
                tempsum = l1.val + tempsum
                l1 = l1.next
            if (l2 != None):
                tempsum = tempsum + l2.val
                l2 = l2.next

            temp.val = tempsum % 10
            tempsum = int(tempsum / 10)

            if l1 == None and l2 == None and tempsum == 0:
                break

            temp.next = ListNode(0)
            temp = temp.next
        return ans


if __name__ == "__main__":
    t1 = ListNode(3)
    t2 = ListNode(4)
    t2.next = t1
    t3 = ListNode(2)
    t3.next = t2
    b1 = ListNode(4)
    b2 = ListNode(6)
    b2.next = b1
    b3 = ListNode(5)
    b3.next = b2

    result = Solution()
    add_sum = result.addTwoNumbers(t3, b3)

    while (add_sum != None):
        print (add_sum.val)
        add_sum = add_sum.next
