#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 10:19 下午
# @Author  : Wentworth.Zhu
# @File    : No_21_merge-two-sorted-lists.py
# @Software: macOS Catalina MBP python3.7


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        # 终止条件
        if not l1 : return l2
        if not l2 : return l1
        # 判断部分
        if l1.val <= l2.val :
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2