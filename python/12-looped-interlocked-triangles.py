import turtle

turtle.up()
turtle.goto(100, 100)
turtle.down()

i = 10
while i < 400:
    turtle.forward(i)
    turtle.left(120)
    i += 10

i = 10
while i <= 400:
    turtle.forward(i)
    turtle.right(120)
    i += 10
