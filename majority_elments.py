# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Site: 
# @File: majority_elments.py
# @Author: zheng
# @Time: 4月 19, 2020
"""
题目：给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [3,2,3]
输出: 3
"""


def majority_element(nums) -> int:
    """
    # hash表计数解法
    :param nums:
    :return:
    """
    hash_vals = {}
    for num in nums:
        if hash_vals.get(num) is not None:
            hash_vals[num] += 1
        else:
            hash_vals[num] = 1
    vals_sort = sorted(hash_vals.items(), key=lambda x:x[1], reverse=True)
    return vals_sort[0][0]


def majorityElement(nums) -> int:
    """
    应用多数投票法 boyer-moore方法：数组中从candidate被赋值到count减到0的那一段可以被去除，余下
    部分的多数元素依然是原数组的多数元素。我们可以不断重复这个过程，直到扫描到数组尾部，那么count必
    然会大于0，而且这个count对应的candinate就是原数组的多数元素。
    :param nums:
    :return:
    """
    candidate = count = 0
    for i in nums:
        if count == 0:
            candidate = i
        if candidate == i:
            count += 1
        else:
            count -= 1
    return candidate


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    val = majority_element(nums)
    print(val)