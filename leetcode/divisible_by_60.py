# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Site: 
# @File: divisible_by_60.py
# @Author: zheng
# @Time: 4月 30, 2020

from itertools import combinations

"""
题目描述：
在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。

返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字 i 和 j 满足  i < j 且有 
(time[i] + time[j]) % 60 == 0。


示例 1：

输入：[30,20,150,100,40]
输出：3
解释：这三对的总持续时间可被 60 整数：
(time[0] = 30, time[2] = 150): 总持续时间 180
(time[1] = 20, time[3] = 100): 总持续时间 120
(time[1] = 20, time[4] = 40): 总持续时间 60

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pairs-of-songs-with-total-durations-divisible-by-60
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:

    # version1  超出时间限制
    def numPairsDivisibleBy60_v1(self, time) -> int:
        combs = combinations(time, 2)
        nums = 0
        for comb in combs:
            if sum(comb) % 60 == 0:
                nums += 1
        return nums

    # 正解
    def numPairsDivisibleBy60(self, time) -> int:
        """
        如果一个数对60的余数为20，则与它配对的数对60的余数必然为40。故只需查看余数为40的数的个数，即为配对数目，
        同时记录余数为20的数的数目。最后统计配对数目总和即可
        :param time:
        :return:
        """
        res_map = [0] * 60
        res = 0
        for t in time:
            t %= 60
            if t == 0:
                res += res_map[0]
            else:
                res += res_map[60-t]
            res_map[t] += 1
        return res




        return nums


if __name__ == "__main__":
    num_pairs = Solution()
    time = [30, 20, 150, 100, 40]
    print(num_pairs.numPairsDivisibleBy60(time=time))

