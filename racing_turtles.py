#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(15):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  backward(200)
  left(90)
  forward(20)

ada = Turtle()
ada.color('tomato')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()
  
bob = Turtle()
bob.color('green')
bob.shape('turtle')
bob.penup()
bob.goto(-160, 70)
bob.pendown()
  
tag = Turtle()
tag.color('turquoise')
tag.shape('turtle')
tag.penup()
tag.goto(-160, 40)
tag.pendown()
  
den = Turtle()
den.color('magenta')
den.shape('turtle')
den.penup()
den.goto(-160, 10)
den.pendown()

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  tag.forward(randint(1,5))
  den.forward(randint(1,5))
  
for turn in range(36):
  ada.right(10)
  bob.right(10)
  tag.right(10)
  den.right(10)