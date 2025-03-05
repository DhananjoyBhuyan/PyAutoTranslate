#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 23:15:17 2025

@author: Dhananjoy Bhuyan
"""

from pyautotranslate import init, execute_code

init("html_testing", ".html", "html")

"""pycode
title_of_page = "Python"

display code block(id = "code_block", content=
```python []
print("Hello World")
```).border_radius = 8px and padding = 10px
code_block.find("print").set_ID("theprinttext")

theprinttext.color = Orange

code_block.find("(", ")").color = White

code_block.background-color = Black

code_block.find('"Hello World"').color = Light Green

code_block.display = "inline-block"


"""

execute_code()
