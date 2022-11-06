import turtle as t

t.title('Lab00 DDP 1')
t.pensize(10)
t.shape('blank')

def left_then_forward(angle: float, units: float):
    t.left(angle)
    t.forward(units)

# Create black background
t.penup()
t.left(90)
t.forward(15)
t.pendown()
t.color('black')
t.begin_fill()
left_then_forward(90, 75)
left_then_forward(90, 130)
left_then_forward(90, 175)
left_then_forward(90, 130)
left_then_forward(90, 100)
t.penup()
t.end_fill()

# Reset pos and put the pen down again to start drawing
t.home()
t.pendown()

# Create the letter "C"
t.color('blue')
t.forward(-50)
left_then_forward(-90, 100)
left_then_forward(90, 50)

# Raise pen, move it by 25 pixels on the x axis, and put it down again
t.penup()
t.forward(25)
t.pendown()

# Create the letter "S"
t.color('red')
t.forward(50)
left_then_forward(90, 50)
left_then_forward(90, 50)
left_then_forward(-90, 50)
left_then_forward(-90, 50)
t.penup()

# Only exit the window when clicked
t.exitonclick()
