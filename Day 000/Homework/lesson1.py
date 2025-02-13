from turtle import*

shape("turtle")

speed(10)
width(4)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(80)
color("gray")
begin_fill()
left(90)
forward(80)
right(90)
forward(35)
right(90)
forward(80)
end_fill()

penup()
goto(200,200)
pendown()

color("brown")

right(150)
begin_fill()
forward(200)
left(120)
forward(200)
end_fill()

left(55)
penup()
goto(20,150)
pendown()

color("yellow")
left(65)
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(180,100)
pendown()

left(90)
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

exitonclick()