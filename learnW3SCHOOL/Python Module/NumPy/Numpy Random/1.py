import math
from turtle import *

def hearta(k) :
    return 15 * math.sin(k)**3
def heartb(k) :
    return 12 * math.cos(k)-5*\
           math.cos(2*k)-2*\
           math.cos(3*k)-\
           math.cos(4*k)

speed(0)
bgcolor("black")

for i in range(10000):
    goto(hearta(i) * 20 , heartb(i) * 20)
    for j in range(5) :
        color("#f73487")
    goto(0,0)
done()

print("---------------------------------------")

# import turtle
# import colorsys

# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor('black')
# t.speed(0)
# n = 50
# h = 0

# for i in range(280) :
#     c = colorsys.hsv_to_rgb(h,1,0.8)
#     h = h + 1/n
#     t.color(c)
#     t.forward(i*2)
#     t.left(145)

# turtle.done()





