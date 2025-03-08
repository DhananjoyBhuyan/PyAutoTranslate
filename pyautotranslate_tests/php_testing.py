#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 00:16:22 2025

@author: Dhananjoy Bhuyan
"""
from pyautotranslate import init, execute_code

init("output_php_file", ".php", "php")

"""pycode

full_form = "the full form of php"

if php_is_a_markup_language == True:
    print("php is a markup language!!")
else:
    print("php is a normal programming language!! Yaaaay!!")
print("Full form of php is: ", full_form)

Note_for_the_interpreter = "Relpace the value of full_form with the actual full form of php"

"""

execute_code()
