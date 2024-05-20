from turtle import *
speed(10)
shape("turtle")
width(7)
begin_fill()
color("brown")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

# draw a door
forward(70)
color("blue")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()


penup()
goto(200, 200)
pendown()


begin_fill()
color("green")
right(150)
forward(200)
left(120)
forward(200)
left(90)
end_fill()
begin_fill()
color("blue")
left(30)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()




penup()
goto(200, 200)
pendown()
begin_fill()
forward(60)
left(90)
forward(60)
left(90)
forward(60)
color("blue")
end_fill()

penup()
goto(200, 200)
pendown()

exitonclick()