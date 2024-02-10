from turtle import *

#we want to paint a house

#step 1: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)

forward(200)
left(90)

#end of square

#draiwing a door

forward(70)
color("yellow")
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(170, 170)
left(33)
pendown()


color("red")
begin_fill()
right(95)
forward(40)
left(95)
forward(40)
left(85)
forward(40)
right(95)

left(190)
forward(40)

penup()
goto(60, 130)
left(90)
pendown()

color("red")
begin_fill()
right(95)
forward(40)
left(95)
forward(40)
left(85)
forward(40)
right(95)

left(190)
forward(40)



exitonclick()