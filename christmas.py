#Christmas greeting message in python (Turtle)


#lets go !!!!


from turtle import *
from random import randint

def create_rectangle(turtle, color , x, y , width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)

    turtle.end_fill()

    turtle.setheading(0)

def create_circle(turtle, x, y, radius, color):
    pyguy.penup()
    pyguy.color(color)
    pyguy.fillcolor(color)
    pyguy.goto(x,y)
    pyguy.pendown()
    pyguy.begin_fill()
    pyguy.circle(radius)
    pyguy.end_fill()

#ummmmmm bg color ???

BG_COLOR = "#ffae00"

pyguy = Turtle()

pyguy.speed(2)
screen = pyguy.getscreen()

screen.bgcolor(BG_COLOR)

screen.title("Merry Christmas")

screen.setup(width= 1.0, height= 1.0)

y = -100

# ok lets create a tree trunk

create_rectangle(pyguy, "brown", -15,y-60,30,60)

#lets create a tree nowwwwwww!!!

width = 240
pyguy.speed(10)
# i want it fast :D

while width > 10:
    width = width -10
    height = 10
    x = 0 - width/2
    create_rectangle(pyguy, "#0ba30e", x , y ,width,height)
    y = y + height

#lets create a star on the top of the treeeeee

pyguy.speed(1)
pyguy.penup()
pyguy.color('yellow')
pyguy.goto(-20, y+10)
pyguy.begin_fill()
pyguy.pendown()
for i in range(5):
    pyguy.forward(40)
    pyguy.right(144)
pyguy.end_fill()

tree_height = y+40

#lets create a moooooon

create_circle(pyguy,230, 180, 60 , "white")
create_circle(pyguy, 220, 180, 60 , BG_COLOR)

#lets add few randow stars in the sky :D

pyguy.speed(10)
number_of_stars = randint(20,30)
for _ in range(0,number_of_stars):
    x_star = randint(-(screen.window_width()//2),screen.window_width()//2)
    y_star = randint(tree_height, screen.window_height()//2)
    size = randint(5,20)
    pyguy.penup()
    pyguy.color('white')
    pyguy.goto(x_star,y_star)
    pyguy.begin_fill()
    pyguy.pendown()
    for i in range(5):
        pyguy.forward(size)
        pyguy.right(144)
    pyguy.end_fill()

#lets write our greeting message :D

pyguy.speed(2)
pyguy.penup()
message = "Merry Christmas To Everyone From PYGUY"
pyguy.goto(1, -200)
pyguy.color("white")
pyguy.pendown()
pyguy.write(message,move = False, align="center",font=("Arial",15,"bold"))

pyguy.hideturtle()
screen.mainloop()

#huh its done lets see how it goes :D
