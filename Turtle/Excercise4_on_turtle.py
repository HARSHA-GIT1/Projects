import turtle
turtle.bgcolor("Black")
pen1= turtle.Turtle()
pen1.speed(0)
pen1.hideturtle()
pen1.goto(-300,50)
pen1.pensize(5)
pen1.pencolor("Blue")
pen1.circle(100)
pen1.penup()
pen1.color("red")

pen1.goto(150,50)
pen1.pendown()
pen1.forward(300)
pen1.lt(90)
pen1.forward(150)
pen1.lt(90)
pen1.forward(300)
pen1.lt(90)
pen1.forward(150)

pen1.penup()
pen1.pencolor("Yellow")
pen1.goto(-220,-300)
pen1.pendown()
pen1.rt(90)
pen1.forward(200)
pen1.rt(120)
pen1.forward(180)
pen1.rt(115)
pen1.forward(185)
pen1.penup()
pen1.pencolor("Orange")
pen1.goto(160,-300)
pen1.pendown()
pen1.lt(55)
pen1.forward(100)
pen1.lt(60)
pen1.forward(90)
pen1.lt(85)
pen1.forward(110)
pen1.lt(70)
pen1.forward(110)
pen1.lt(80)
pen1.forward(90)
pen1.showturtle()
turtle.exitonclick()
