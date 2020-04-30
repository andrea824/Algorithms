# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Site: 
# @File: merge.py
# @Author: zheng
# @Time: 4月 29, 2020

class Merge():

    def sort(self, a, lo, mid, hi):
        """
        原地归并
        :return:
        """
        i = lo
        j = mid+1
        aux = a
        for k in range(hi):
            if i > mid:
                j += 1
                a[k] = aux[j]
            elif j > hi:
                i += 1
                a[k] = aux[i]
            elif aux[j] < aux[i]:
                j += 1
                a[k] = aux[j]
            else:
                i += 1
                a[k] = aux[i]
        return a

if __name__ == '__main__':
    select = Merge()
    nums = [6, 4, 10, 9, 7, 7, 9, 10]
    print(select.sort(nums, lo=0, mid=4, hi=7))