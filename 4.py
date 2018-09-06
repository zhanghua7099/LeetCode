'''
题目：两个排序数组的中位数
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。
你可以假设 nums1 和 nums2 不同时为空。
'''
'''
示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
中位数是 (2 + 3)/2 = 2.5
'''
#注：本算法时间复杂度不是O(log(m+n))


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m = len(nums1)
    n = len(nums2)
    index1 = 0
    index2 = 0
    lst = []
    while index1 < m and index2 < n:
        if nums1[index1] < nums2[index2]:
            lst.append(nums1[index1])
            index1 += 1
        else:
            lst.append(nums2[index2])
            index2 += 1
    while m > index1:
        lst.append(nums1[index1])
        index1 += 1
    while n > index2:
        lst.append(nums2[index2])
        index2 += 1
    if (m+n) % 2 != 0:
        return lst[int((m+n)/2)]
    else:
        return (lst[int((m+n)/2)-1]+lst[int((m+n)/2)])/2


print(findMedianSortedArrays([1,3], [2,4]))
