#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 10:15 下午
# @Author  : Wentworth.Zhu
# @File    : No_15_3sum.py
# @Software: macOS Catalina MBP python3.7

class Solution:
    def threeSum(self, nums):
        # 1/枚举 暴力嵌套，ijk, O(n^3)
        # 2/枚举 两数之和=0 搭配0，两数之和!=0，找其相反数，O(n^2)
        Final = []
        nums.sort()
        if len(nums)<3:
            return []
        for i in range(len(nums)-2) :
            j,last_item = i+1 , len(nums)-1
            if (i>0 and nums[i] == nums[i-1]) :
                continue
            else:
                while j< last_item :
                    target = nums[i] * -1
                    if nums[j] + nums[last_item] < target:
                        j +=1
                    elif nums[j] + nums[last_item] > target :
                        last_item -=1
                    else :
                        answear = [nums[i],nums[j],nums[last_item]]
                        Final.append(answear)
                        while (j < last_item and nums[j] == nums[j+1]):
                            j +=1
                        while (last_item > j and nums[last_item] == nums[last_item-1]):
                            last_item -=1
                        j +=1
        return Final