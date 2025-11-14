# =====================================
# Author: Oliver T
# Date: 10/21/2025
# Description: A graphing calculator made in python using turtle graphics
# =====================================

# Module imports
import turtle
import math

# Function to create the grid
def create_gird(screen_size = 300, grid_increments = 5):
    '''
    Draws the graph grid using the turtle
    ### Parameters:
    - screen_size: How big the screen size is in pixels
    - grid_increments: How many grids will be in each positive and negative direction
    '''
    grid_increments = int(screen_size / (grid_increments*2)) # Converts it to a number of grids total
    print('Creating grid...')
    start_pos = [-1,1] # X and Y direction
    for pos in start_pos:
        t.penup()
        t.goto(screen_size * pos, screen_size) # Goes to top left corner
        t.right(90) # Faces down
        increment = int(screen_size/grid_increments)
        for i in range(increment): # repeats for amount of grids in a direction
            if i == int(increment/2):
                t.pencolor(0,0,0)
            else:
                t.pencolor(212, 212, 212)
            t.pendown()
            t.forward(screen_size*2) # moves down by screen size
            t.penup()
            t.left(90) # faces right
            t.forward(grid_increments) # forward by grid increment
            t.left(90) # faces up
            t.pencolor(212, 212, 212)
            t.pendown()
            t.forward(screen_size*2) # moves down by screen size
            t.penup()
            t.right(90) # faces right
            t.forward(grid_increments) # forward by grid increment
            t.right(90) # faces down
    t.penup()

# Function to draw a sine wave using the turtle module
def draw_sine(A = 1, B = 1, c = 0, d = 0):
    print(f'Graphing: y = "{A/grid_step_pixels}sin({B/grid_step_pixels}(x-{c/grid_step_pixels}))+{d/grid_step_pixels}" ...')    
    t.pencolor(0,0,0)
    coordinates = int(window_size/2)
    for x in range(-coordinates, coordinates):
        x_coords = (x / (grid_step_pixels / 2)) # This is to get 1 x value to be the grid increment
        c_coords = (c / (grid_step_pixels / 2)) # Same here
        t.goto(
            x = x, 
            y = A * math.sin(B*(x_coords - c_coords)) + d
            #y = A * math.sin((x+horizontal_shift)/(2*math.pi/(B))) + vertical_shift
            )
        t.pendown()
    t.penup()
    print('Graph complete, click anywhere on window to close')

# Function to draw a linear function using the turtle module
def draw_line(slope = 1, y_int = 0):
    print(f'Graphing: "y = {slope}x + {y_int/grid_step_pixels}"')
    #t.goto(x = -int((window_size/2)/slope), y = 0)
    t.pencolor(0,0,0)
    for x in range(-int(window_size/2), int(window_size/2)):
        #print(x)
        t.goto(x = x, y = slope * x + (y_int))
        t.pendown()

# Function to obtain a valid number from the user
def get_number(prompt, min, max):
    '''
    Function to obtain a valid number form the user
    ### Parameters
    - prompt (str): The message displayed to the user
    - min (int): The smallest number the user is allowed to enter
    - max (int): The biggest number the user is allowed to enter
    ### Returns:
    int: number user passed in | None: if the user just clicked enter
    '''

    # Repeats until a valid response from the user is given
    while True:
        # Initializes a flag for if the number the user entered is negative
        negative_flag = False
        print(prompt) # Prints the prompt passed in
        num = input(f'Min = {min}, Max = {max}: ') # Gets user input
        
        # Checks if user entered nothing
        if num == '':
            return None
        
        # Checks if the first character is a negative sign
        if num[0] == '-':
            # Removes it and changes the flag, so it can be returned as a negative int
            num = num.strip('-')
            negative_flag = True
        
        # Checks if the number is a positive int
        if num.isnumeric():
            if negative_flag:
                num = -int(num)
            if int(num) >= min and int(num) <= max:
                print(f'----> Setting changed to: {num}')
                return int(num) # Returns the valid int the user passed in
        
        # Continues the loop if no valid input was given
        else:
            continue

# Welcome screen
print("""Welcome to Turtle Graphing Calculator
Select Mode:
1. Sine graph
2. Linear function""")

# Asks for the menu option
choice = get_number('Enter choice', 1, 2)

if choice:
    # Graph window initialization
    print('-----------------------------------------')
    print('Initialize viewport settings (For default value, simply press enter)')
    print('Enter the viewport size (Keep in mind, the larger the number, the slower it gets graphed)')
    window_size = get_number('Screen size px (Default 200px)', 100, 1080)
    window_size = window_size if window_size else 200 # If the user put nothing it sets it to 300
    print('-----------------------------------------')
    print('Enter the amount of zoom you want applied to the graph\n(Eg. a zoom of 5 will show a 10 by 10 grid)')
    grid_step = get_number('Enter zoom (Default 5)',1, int(window_size/4))
    grid_step = grid_step if grid_step else 5
    grid_step_pixels = int(window_size / (grid_step*2))

# Sine Graph Mode
if choice == 1:
    print('--- Sine graph mode ---\nType in the values (Click enter for the default value)')
    
    # Sine wave amplitude
    amp = get_number(f'Amplitude (Default 1)', 1, int(window_size/2))
    amp = (amp if amp else 1) * grid_step_pixels # Multiplies it by the grid increment pixels so 1 grid unit equals to 1 y value
    
    # Sine wave period
    period = get_number('Period/frequency (Default 1)', 1, window_size)
    period = (period if period else 1)# * grid_step_pixels#int((window_size/math.pi)/2)

    # Sine wave horizontal shift
    h_shift = get_number('Horizontal shift (Default 0)', -grid_step, grid_step)
    h_shift = (h_shift if h_shift else 0) * grid_step_pixels
    #h_shift *= grid_step_pixels

    v_shift = get_number('Vertical shift (Default 0)', -grid_step, grid_step)
    v_shift = (v_shift if v_shift else 0) * grid_step_pixels
    #v_shift *= grid_step_pixels

    # Necessary Turtle initializations 
    t = turtle.Turtle()
    t.screen.title('Sine Graph Mode')
    turtle.colormode(255)
    t.speed(0)
    screen = turtle.Screen()
    screen.setup(width=window_size, height=window_size)
     
    create_gird(window_size, grid_step)
    draw_sine(amp, period, h_shift, v_shift)
    
    turtle.exitonclick()

# Linear function mode
if choice == 2:
    print('--- Linear function mode ---\nType in the values (Click enter for the default value)')
    
    slope = get_number('Slope (Default 1)', -100, 100)
    slope = slope if slope else 1
    y_intercept = get_number('Y intercept (Default 0)', -window_size, window_size)
    y_intercept = (y_intercept if y_intercept else 0) * grid_step_pixels

    # Necessary Turtle initializations 
    t = turtle.Turtle()
    t.screen.title('Linear Function Mode')
    turtle.colormode(255)
    t.speed(0)
    screen = turtle.Screen()
    screen.setup(width=window_size, height=window_size)

    create_gird(window_size, grid_step)
    draw_line(slope, y_intercept)
    
    turtle.exitonclick()
    

