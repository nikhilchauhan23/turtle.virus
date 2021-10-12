#Import turtle library 
import turtle

#  create a screen

screen = turtle.Screen()

# create a drawer for drawing

drawer = turtle.Turtle()

#set the background color of screen 
screen.bgcolor("black")

# for set a background, color, speed, pensize and color of drawer.

drawer.pencolor("dark green")

drawer.pensize(3)

drawer1 = 0

drawer2 = 0

drawer.speed(0)

drawer.goto(0, 200)

drawer.pendown()

# create whille loop for drawing corona virus shape.

while True:

    drawer.forward(drawer1)

    drawer.right(drawer2)

    drawer1 += 3

    drawer2 += 1

    if drawer2 == 210:

       break

    # for hide a drawer

drawer.ht()

# for holding the mainscreen

screen.mainloop()