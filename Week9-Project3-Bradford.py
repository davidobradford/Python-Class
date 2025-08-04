"""
Program: Week9-Project3-Bradford.py
Author: David Bradford
Due Date: 07/22/25
Semester: Spring 2025
Instructor: Mark Pranger
Function draws a the first three levels of a Koch snowflake using
the Turtle Graphics module.
"""
import math
from turtle import Turtle


##def drawCircle(t, x, y, radius):
##    t.up()
##    t.goto(x, y)
##    t.down()
##    t.up()
##    t.setheading(90)
##    t.forward(radius)
##    t.setheading(0)
##    distance = 2.0 * math.pi * radius / 120.0
##    t.down()
##    for count in range(120):
##        t.right(3)
##        t.forward(distance)

def drawFractalLine(t, lev, angle, distance, ctr):    
    t.left(angle)
    t.forward(distance)

    ctr += 1
    if lev == 0 and ctr == 3:
        return 0
    elif lev == 1 and ctr == 12:
        return 0
    elif lev == 2 and ctr == 48:
        return 0
    else:
        if lev == 1:
            angle = angle * -1 
        drawFractalLine(t, lev, angle, distance, ctr)
        


def main():
    t = Turtle()
##    x = int(input("Enter the X Coordinate For the Center of the Circle To Draw: "))    
##    y = int(input("Enter the Y Coordinate For the Center of the Circle To Draw: "))
##    rad = int(input("Enter the Raduius Of the Circle To Draw: "))
    lev = 1
    ang = 120
    dist = 200
    ctr = 0
    
    q = (dist * math.sqrt(3)) / 6
    t.up()
    t.goto(0, 0)
    t.setheading(90)
    t.forward(q)
    t.setheading(0)
    t.forward(dist / 2)
    t.setheading(60)
    t.down()

    if lev == 1:
        dist = math.ceil(dist / 3)
    if lev == 2:
        dist = math.ceil(dist / 6)

    t.left(ang)
    t.forward(dist)

    if lev == 0:
        ang = 120
    if lev == 1:
        ang = -60

    t.left(ang)
    t.forward(dist)

    

    if lev != 0:
        ang = ang * -1 
        
    t.left(ang)
    
    drawFractalLine(t, lev, ang, dist, ctr)

if __name__ == "__main__":
    main()

