from turtle import *
import turtle 

t = turtle.Turtle()
turtle.screensize(960, 720, "black")
t.width(1)

t.speed(0)

for x in range(300):

	if x % 5 == 0:
		t.color("cadetblue")

	if x % 5 == 1:
		t.color("lightsteelblue")

	if x % 5 == 2:
		t.color("powderblue")

	if x % 5 == 3:
		t.color("mediumaquamarine")

	if x % 5 == 4:
		t.color("aquamarine")

	t.forward(x * 2)
	t.left(89)




