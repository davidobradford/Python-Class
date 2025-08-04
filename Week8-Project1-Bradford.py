"""
Program: Week9-Project1-Bradford.py
Author: David Bradford
Due Date: 07/22/25
Semester: Spring 2025
Instructor: Mark Pranger
Function draws a circle using the Turtle Graphics module.
"""
import math
from turtle import Turtle

def drawCircle(t, x, y, radius):
    t.up()
    t.goto(x, y)
    t.down()
    t.up()
    t.setheading(90)
    t.forward(radius)
    t.setheading(0)
    distance = 2.0 * math.pi * radius / 120.0
    t.down()
    for count in range(120):
        t.right(3)
        t.forward(distance)

def main():
    t = Turtle()
    t.hideturtle()
    x = int(input("Enter the X Coordinate For the Center of the Circle To Draw: "))    
    y = int(input("Enter the Y Coordinate For the Center of the Circle To Draw: "))
    rad = int(input("Enter the Raduius Of the Circle To Draw: "))
    drawCircle(t, x, y, rad)

if __name__ == "__main__":
    main()

