import turtle as t
from random import randint
from tkinter import messagebox
from math import ceil

# Initialize turtle config and default outer brick color
OUTER_BRICK_COLOR = '#BC4A3C'
t.pensize(1)
t.color('#000000')
t.bgcolor('#FFAC8D')
t.colormode(255)
t.speed(10)
t.shape('turtle')
t.tilt(45)
t.setup(.75, .90)
t.screensize(1280, 720)

# Get user input for the amount of bricks 
# on the lowest and top most layer
lower_layer_bricks = int(t.numinput("Lowest Layer", 
                                    "Amount of bricks for the lowest layer"
                                    "\nDecimals will be floored/rounded down",
                                    minval=1, 
                                    maxval=25))

upper_layer_bricks = int(t.numinput("Top Most Layer", 
                                    "Amount of bricks for the top most layer"
                                    "\nDecimals will be floored/rounded down",
                                    minval=1, 
                                    maxval=25))

# Validate if the lowest layer has more bricks than the top most layer
# If not, show a warning and asks if the user want to swap the value
# If the user doesn't want to swap, 
# ask the user to input the brick amount again
while lower_layer_bricks < upper_layer_bricks:
    messagebox.showwarning("Invalid Input", 
                           "The bricks on the lower layer "
                           "cannot be lower than the top most layer")

    swap = messagebox.askyesno("Swap?", 
                               "Do you want to swap the top most "
                               "and the lowest brick amount?")

    if swap:
        lower_layer_bricks, upper_layer_bricks = upper_layer_bricks, \
                                                 lower_layer_bricks
    
    else:
        lower_layer_bricks = int(t.numinput("Lowest Layer", 
                                            "Amount of bricks "
                                            "for the lowest layer\n"
                                            "Decimals will be "
                                            "floored/rounded down", 
                                            minval=1, 
                                            maxval=25))

        upper_layer_bricks = int(t.numinput("Top Most Layer", 
                                            "Amount of bricks "
                                            "for the top most layer\n"
                                            "Decimals will be "
                                            "floored/rounded down",
                                            minval=1, 
                                            maxval=25))

# Get user input for the length and width of the bricks in pixels
brick_length = int(t.numinput("Brick Length", 
                              "The length of 1 brick (in pixels)\n"
                              "Decimals will be floored/rounded down",
                              minval=1, 
                              maxval=35))

brick_width  = int(t.numinput("Brick Width", 
                              "The width of 1 brick (in pixels)\n"
                              "Decimals will be floored/rounded down",
                              minval=1, 
                              maxval=25))

# Validate if the brick length is bigger than its width
# If not, show a warning and asks if the user want to swap the value
# If the user doesn't want to swap, 
# ask the user to input the length and width of the bricks again
while brick_length < brick_width:
    messagebox.showwarning("Invalid Input", 
                           "The length of the bricks "
                           "cannot be shorter than the width")

    swap = messagebox.askyesno("Swap?", 
                               "Do you want to swap the length "
                               "and the width?")
    
    if swap:
        brick_length, brick_width = brick_width, brick_length

    else:
        brick_length = int(t.numinput("Brick Length", 
                                      "The length of 1 brick (in pixels)\n"
                                      "Decimals will be floored/rounded down",
                                      minval=1, 
                                      maxval=35))

        brick_width  = int(t.numinput("Brick Width",
                                      "The width of 1 brick (in pixels)\n"
                                      "Decimals will be floored/rounded down",
                                      minval=1,
                                      maxval=25))   

# Initialize variable for loop and ending text
total_layer = lower_layer_bricks - upper_layer_bricks
current_layer_length = lower_layer_bricks * brick_length
total_height = total_layer * brick_width
current_layer_brick = lower_layer_bricks

text_pos = total_height
brick_count = 0

# Runs until the current layer is the same
# as the total layer of the temple
for current_layer in range(total_layer + 1):
    """Sets the pen's position so that the final
    temple drawing is in the middle of the canvas.
    
    For the x position,
    Current layer length is divided by 2, rounded
    up, and turned into a negative so the temple
    is centered horizontally in the canvas.

    For the y position,
    Total height is divided by 2, rounded up, and
    also turned into a negative so the temple is
    centered vertically.
    """
    t.penup()
    t.setposition(-(ceil(current_layer_length/2)),
                  -(ceil(total_height/2)))

    # Loop to draw the bricks on current layer
    for i in range(current_layer_brick):

        # Random color for every brick that is not 
        # on the outer layer of the temple
        t.fillcolor((randint(0, 255),
                     randint(0, 255),
                     randint(0, 255)))
        
        # Checks if the brick that is going to be drawn 
        # is on the lowest or top most layer,
        # or is the outer bricks of the current layer
        if current_layer == 0 or current_layer == total_layer \
           or i == 0 or i == current_layer_brick-1:
            t.fillcolor(OUTER_BRICK_COLOR)
        
        t.pendown()
        t.begin_fill()
        t.forward(brick_length)
        t.left(90)
        t.forward(brick_width)
        t.left(90)
        t.forward(brick_length)
        t.left(90)
        t.forward(brick_width)
        t.end_fill()
        t.penup()
        t.left(90)
        t.forward(brick_length)
        brick_count += 1
    
    # After all the bricks on the current layer is drawn,
    # reduce the layer length by a brick's length,
    # reduce the amount of brick in the current layer by 1,
    # and also raise the layer by 1
    current_layer_length -= brick_length
    total_height -= brick_width * 2
    current_layer_brick -= 1

# After all the drawing is done, hide the pen,
# and sets the pen's position such that it is 25 pixels
# below the temple and write how many bricks is used.
t.ht()
t.setposition(0, -(ceil(text_pos/2) + 25))
t.write(f'A Colorful Temple made with {brick_count} bricks '
         'and love (´▽`ʃ♡ƪ)', 
          align='center', 
          font=('Times New Roman', 12, 'normal'))

t.exitonclick()
