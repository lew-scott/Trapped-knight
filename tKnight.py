# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:35:31 2019

@author: pm11lms
"""
from moveKnight import getMoves as m
import turtle


# creates matrix, moves knight and records positions 
moves = m()
for i in range(0, len(moves)):
    if(moves[i][1] > 35):
        moves[i][1] = 35 - moves[i][1] + 35
    elif(moves[i][1] < 35):
        moves[i][1] = 35 + 35 - moves[i][1]

t = turtle.Turtle()
t.screen.setworldcoordinates(0,0,70,70)



def draw():
    t = turtle.Turtle()
    t.ht()
    t.penup()
    t.setpos((35,35))
    t.speed(10)
    t.width(2)
    t.pendown()  
    for i in range(1, len(moves)):
        t.goto(moves[i][0],moves[i][1])
        if i > 1700:
            t.color("#e8682e")
        elif i > 1200:
            t.color("#f2e64b")
        elif i > 600:
            t.color("#4fa78f")
        else:
            t.color("#003366")


draw()
t.screen.exitonclick()
