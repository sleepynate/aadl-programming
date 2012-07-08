import turtle

# move the cursor to where the top-right corner should be if we're centered
turtle.up()
turtle.goto(-50, 50)

# draw the top of the square
turtle.down()
turtle.forward(100)

# draw the right side of the square
turtle.right(90)
turtle.forward(100)

# draw the bottom of the square
turtle.right(90)
turtle.forward(100)

# draw the left side
turtle.right(90)
turtle.forward(100)
