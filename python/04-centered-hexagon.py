import turtle

# move the cursor to where the top-right corner should be if we're centered
turtle.up()
turtle.goto(-50, 50)

# draw the top of the hexagon
turtle.down()
turtle.forward(100)

# draw the right upper side of the hexagon
turtle.right(60)
turtle.forward(100)

# draw the right lower side of the hexagon
turtle.right(60)
turtle.forward(100)

# draw the bottom of the hexagon
turtle.right(60)
turtle.forward(100)

# draw the left lower side of the hexagon
turtle.right(60)
turtle.forward(100)

# draw the left upper side of the hexagon
turtle.right(60)
turtle.forward(100)

