#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:38:58 2025

@author: Dhananjoy Bhuyan
"""
import pyautotranslate

pyautotranslate.init("c_testing", "c", "c")

"""pycode
define A = integer_array([
    ["item1", "item2"],
    ["item3", "item4"],
    ["item5", "item6"]
    ], type="2D array")

for i in A:
    print(A[i])
    for j in i:
        print(A[i][j])

"""

pyautotranslate.execute_code()
