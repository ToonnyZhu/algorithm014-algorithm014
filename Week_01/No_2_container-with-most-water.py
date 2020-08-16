#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 10:13 下午
# @Author  : Wentworth.Zhu
# @File    : No_2_container-with-most-water.py
# @Software: macOS Catalina MBP python3.7


class Solution:
    def maxArea(self, height):
    # 1/枚举，暴力求解
        # max_value = 0
        # for i in range(len(height)-1):
        #     for j in range(i,len(height)):
        #         area = (j-i) * min(height[i],height[j])
        #         max_value = max(max_value,area)
        # return max_value

    # 2/两侧收敛
        max_value = 0
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] < height[j]:
                area = (j - i) * height[i]
                max_value = max(max_value, area)
                i += 1
            else:
                area = (j - i) * height[j]
                max_value = max(max_value, area)
                j -= 1
        return max_value