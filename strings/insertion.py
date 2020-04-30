# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Site: 
# @File: insertion.py
# @Author: zheng
# @Time: 4月 28, 2020


class Insertion():

    def sort(self, nums):
        length = len(nums)
        for i in range(1, length):
            for j in range(i, 0, -1):
                if j > 0 and nums[j] < nums[j-1]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]

        return nums

if __name__ == '__main__':
    select = Insertion()
    nums = [6, 4, 10, 9, 7, 7, 9, 10]
    print(select.sort(nums))

