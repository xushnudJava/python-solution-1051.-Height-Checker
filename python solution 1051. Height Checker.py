# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 13:24:19 2023

@author: zero
"""

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        15.01.2023 Sun 1:22 AM
        @author Xomidov Xushnud
        """
        qiymat = 0
        arr = sorted(heights)
        # sorted metodi yoradmi boshqa list osish tartibida joylashtiramiz
        for i in range(len(arr)):
            if arr[i] != heights[i]:
                # sort qilingan list bilan berilgan listdagi 
                # nechta element teng emasligini qiymatga bir qo'shish
                # orqali bilamiz
                qiymat += 1
        return qiymat
        # eng oxirida qiymatni qaytaramiz