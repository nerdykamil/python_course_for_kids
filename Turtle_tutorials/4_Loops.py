# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 11:12:00 2023

@author: Yusra Shahid
"""

import turtle

s = turtle.getscreen()

t = turtle.Turtle()

## draw a square

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

## draw square with for loop
for i in range(4):
    t.forward(100)
    t.right(90)
    
    
## draw circles with while loop

n = 10
while ( n<= 40):
    t.circle(n)
    n = n+10
    

    

    