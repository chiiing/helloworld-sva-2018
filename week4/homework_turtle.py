from turtle import *
import turtle 

t = turtle.Turtle()

t.width(1)

t.speed(0)

for x in range(300):

	if x % 4 == 0:
		t.color("cadetblue")

	if x % 4 == 1:
		t.color("lightsteelblue")

	if x % 4 == 2:
		t.color("powderblue")

	if x % 4 == 3:
		t.color("mediumaquamarine")

	t.forward(x * 2)
	t.left(89)




