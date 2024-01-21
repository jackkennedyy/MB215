import turtle
import tkinter.simpledialog as simpledialog

# Set up the window
window = turtle.Screen()
window.title("Turtle Drawing")

# Create a turtle
my_turtle = turtle.Turtle()

# Set pen size to 3
my_turtle.pensize(3)

# Set drawing color to blue
my_turtle.pencolor("blue")

# Move the turtle forward by 100 units
my_turtle.forward(100)

# Turn the turtle right by 90 degrees
my_turtle.right(90)

# Move the turtle forward by 50 units
my_turtle.forward(50)

# Turn the turtle left by 90 degrees
my_turtle.left(90)

# Lift the pen up – no drawing when moving
my_turtle.penup()

# Move the turtle to a specific location
my_turtle.goto(-50, -50)

# Put the pen down – drawing when moving
my_turtle.pendown()

# Draw a circle with radius of 25
my_turtle.circle(25)

# Draw a dot with diameter 10
my_turtle.dot(10)

# Set the turtle heading to 0 (East)
my_turtle.setheading(0)

# Change the turtle color
my_turtle.color("red")  # Changes pen and fill color

# Draw a filled shape
my_turtle.begin_fill()
my_turtle.circle(50)  # Drawing circle to fill
my_turtle.end_fill()

# Clear the drawing
my_turtle.clear()

# Reset the turtle's state
my_turtle.reset()

# Hide the turtle
my_turtle.hideturtle()

# Display the turtle
my_turtle.showturtle()

# Set the animation speed (0:fastest, 1:slowest, 10:normal)
my_turtle.speed(10)

# Display text
my_turtle.goto(-100,100)
my_turtle.write("Hello Turtle!", font=("Arial", 16, "normal"))

# Get input with a dialog box
user_input = simpledialog.askstring("Input", "Enter your name: ")

# Respond to user input
my_turtle.write(f"Hello, {user_input}!", font=("Arial", 32, "normal"))

# Filling a shape with color
my_turtle.fillcolor("green")
my_turtle.begin_fill()
my_turtle.circle(30)
my_turtle.end_fill()

# Close the window on a click
window.exitonclick()
