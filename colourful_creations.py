#!/bin/python3

from turtle import *

colors = {
  'verylime': '#A7E30E',
  'maroon': '#C31818',
  'green': '#114E08',
  'blue': '#F7F553'
}

screen = Screen()
screen.setup(400, 400)

color(colors['blue'])
dot(300)
screen.bgcolor(colors['verylime'])

penup()
color(colors['maroon'])
style = ('Arial', 40, 'bold')
write('MAZE', font = style, align = 'center')
right(90)
forward(60)

color(colors['green'])
style = ('Verdana', 40, 'bold')
write('Runner', font = style, align = 'center')
hideturtle()