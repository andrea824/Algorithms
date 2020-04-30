# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Site: 
# @File: find_median_from_two_array.py
# @Author: zheng
# @Time: 4月 30, 2020
import math


"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        """
        利用归并排序的思路，将两个数组归并
        """
        length1 = len(nums1)
        length2 = len(nums2)
        totals = length1 + length2
        new_ar = [0] * (totals)
        i, j = 0, 0
        for k in range(totals):
            if j >= len(nums2):
                new_ar[k] = nums1[i]
                i += 1
            elif i >= len(nums1):
                new_ar[k] = nums2[j]
                j += 1
            else:
                if nums1[i] < nums2[j]:
                    new_ar[k] = nums1[i]
                    i += 1
                else:
                    new_ar[k] = nums2[j]
                    j += 1

        return self.find_median(new_ar)

    def find_median(self, nums):
        half = len(nums) // 2
        return (nums[half] + nums[~half]) // 2

if __name__ == '__main__':
    select = Solution()
    nums = [6, 7, 9, 10]
    nums2 = [3, 5, 11]
    print(select.findMedianSortedArrays(nums, nums2))
