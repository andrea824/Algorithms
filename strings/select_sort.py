# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Site: 
# @File: select_sort.py
# @Author: zheng
# @Time: 4月 28, 2020

class Selection():
    """
    选择排序
    """
    def sort(self, nums):
        length = len(nums)
        for i in range(length):
            min = i
            for j in range(i + 1, length):
                if nums[j] < nums[min]:
                    min = j
            nums[i], nums[min] = nums[min], nums[i]
        return nums


if __name__ == '__main__':
    select = Selection()
    nums = [6, 4, 10, 9, 7, 7, 9, 10]
    print(select.sort(nums))
