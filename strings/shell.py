# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Site: 
# @File: shell.py
# @Author: zheng
# @Time: 4月 28, 2020

class Shell():

    def sort(self, nums):
        length = len(nums)
        h = 1
        while h < length / 3:
            h = 3*h + 1
        while h >= 1:
            for i in range(h, length):
                for j in range(i, h-1, -h):
                    if nums[j] < nums[j-h]:
                        nums[j], nums[j-h] = nums[j-h], nums[j]
            h = int(h/3)
        return nums


if __name__ == '__main__':
    select = Shell()
    nums = [8, 9, 1, 7, 2, 3, 5, 4, 6, 0]
    print(select.sort(nums))