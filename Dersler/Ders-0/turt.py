import turtle
import time

# Set up the turtle environment
screen = turtle.Screen()
screen.setup(width=900, height=450)
screen.bgcolor("black")
screen.title("NOVA ACADEMY")

root = screen.getcanvas().winfo_toplevel()

# Set the window's position on the monitor
window_x = 800  # Adjust these values as needed
window_y = 50  # Adjust these values as needed
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
root.geometry(f"+{window_x}+{window_y}")

# Create a Turtle object
t = turtle.Turtle()
t.speed(1000)  # Set the fastest drawing speed
t.color("white")

# Define a function to draw a letter "N"
# Define a function to draw a letter "N"
def draw_N():
    t.penup()
    t.goto(-400, -100)
    t.pendown()
    t.left(90)
    t.forward(200)
    t.right(135)
    t.forward(280)
    t.left(135)
    t.forward(200)

# Define a function to draw a letter "O"
def draw_O():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.circle(100)

# Define a function to draw a letter "V"
def draw_V():
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.right(160)
    t.forward(225)
    t.left(140)
    t.forward(225)

# Define a function to draw a letter "A"
def draw_A():
    t.penup()
    t.goto(130, -100)
    t.pendown()
    t.right(10)
    t.forward(225)
    t.right(125)
    t.forward(225)
    t.backward(112)
    t.right(115)  # Adjusted the angle to make the letter "A" upright
    t.forward(100)

# Draw the letters "NOVA"
for i in range(10):
	t.width(20)
	t.color(colors[i % len(colors)])
	draw_N()
	time.sleep(0.5)
	draw_O()
	time.sleep(0.5)
	draw_V()
	time.sleep(0.5)
	draw_A()
	time.sleep(.5)
	t.reset()

# Hide the turtle and keep the window open
t.hideturtle()
turtle.done()
