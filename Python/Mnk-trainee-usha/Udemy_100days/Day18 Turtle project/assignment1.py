from turtle import Turtle,Screen
a=Turtle()
s=Screen()
a.penup()
a.shape("turtle")
a.goto(-200,100)
a.pensize(5)
a.pencolor("Yellow")
a.pendown()
a.circle(80)

a.right(90)
a.penup()
a.forward(100)
a.pendown()
a.left(30)
a.pencolor("green")
a.forward(150)
a.right(120)
a.forward(150)
a.right(120)
a.forward(150)

a.penup()
a.goto(180,100)
a.pendown()
a.right(60)
a.pencolor("red")
a.forward(150)
a.left(90)
a.forward(150)
a.left(90)
a.forward(150)
a.left(90)
a.forward(150)

a.penup()
s.exitonclick()