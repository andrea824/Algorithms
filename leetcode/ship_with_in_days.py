# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Site: 
# @File: ship_with_in_days.py
# @Author: zheng
# @Time: 4月 30, 2020
import sys

"""
传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

 

示例 1：

输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
class Solution:

    def can_ship(self, weights, D, K):
        """
        判定在承载力为K的情况下，是否能在D天内运完
        :param weights: 货物重量列表
        :param D: 规定的D天
        :param K: 承载力
        :return:
        """
        cur = K  # cur表示当前船的可用承载量
        for weight in weights:
            if weight > K:
                return False
            if cur < weight:
                cur = K
                D -= 1
            cur -= weight
        return D > 0

    def ship_with_in_days(self, weigths, D):
        lo = max(weigths)
        hi = sum(weigths)
        while lo < hi:
            mid = (lo + hi) / 2
            if self.can_ship(weigths, D, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo



