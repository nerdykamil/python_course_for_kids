# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 10:37:06 2023

@author: Yusra Shahid
"""

import turtle

s= turtle.getscreen()

t = turtle.Turtle()

## draw a dot

t.dot(30)

t.reset()

## draw a circle

t.circle(60)


## draw a square

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

turtle.bye()
