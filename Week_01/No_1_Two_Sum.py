#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 8:35 下午
# @Author  : Wentworth.Zhu
# @File    : No_1_Two_Sum.py
# @Software: macOS Catalina MBP python3.7

class Solution:
    def twoSum(self, nums, target) :
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i, hashmap.get(target - num)]
            hashmap[num] = i
