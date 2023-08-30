# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 11:30:08 2023

@author: Yusra Shahid
"""

import turtle

s= turtle.getscreen()

t = turtle.Turtle()

number = 50


if number == 50:
    t.circle(number)


if number <= 50:
    t.circle(number)
    
else:
    print("Please select a number less than 50")
    

number = 80

if number == 50:
    t.circle(number)
    
elif number == 80:
    t.circle(number)
    
else:
    print("Please select a number between 80 and 50")


turtle.bye()