import turtle
import random
import multiprocessing

# Function to draw a colorful star
def draw_star(turtle_name):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for _ in range(5):
        turtle_name.color(random.choice(colors))
        turtle_name.forward(100)
        turtle_name.right(144)

# Create multiple Turtle objects
def create_turtles(num_turtles):
    turtles = []
    for _ in range(num_turtles):
        t = turtle.Turtle()
        t.speed(0)
        turtles.append(t)
    return turtles

# Function to draw stars using multiple Turtle objects
def draw_stars(num_stars):
    turtles = create_turtles(num_stars)
    for t in turtles:
        draw_star(t)

if __name__ == "__main__":
    # Number of stars to draw
    num_stars = 6

    # Create a multiprocessing pool
    pool = multiprocessing.Pool()

    # Draw stars using multiple processes
    pool.map(draw_stars, [num_stars] * num_stars)

    # Close the pool
    pool.close()
    pool.join()

    # Keep the window open
    turtle.done()
