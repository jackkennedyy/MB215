import turtle

def draw_square(side_length, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    turtle.end_fill()

def draw_triangle(side_length, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(side_length)
        turtle.right(120)
    turtle.end_fill()

def draw_circle(radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def get_shape_choice():
    print("Select the shape to draw:")
    print("1 - Square")
    print("2 - Triangle")
    print("3 - Circle")
    print("4 - Rectangle")
    return input("Enter your choice (or 0 to exit): ")

def main():
    turtle.speed(3)  # Set a comfortable drawing speed
    turtle.Screen().bgcolor("white")  # Set background color of the Turtle window
    print("Welcome to the Turtle Geometric Shapes Drawing Program!\n")
    
    while True:
        choice = get_shape_choice()
        
        if choice == "0":
            break
        elif choice == "1":
            side_length = int(input("Enter the side length of the square: "))
            color = input("Enter the color for the square: ")
            draw_square(side_length, color)
        elif choice == "2":
            side_length = int(input("Enter the side length of the triangle: "))
            color = input("Enter the color for the triangle: ")
            draw_triangle(side_length, color)
        elif choice == "3":
            radius = int(input("Enter the radius of the circle: "))
            color = input("Enter the color for the circle: ")
            draw_circle(radius, color)
        elif choice == "4":
            width = int(input("Enter the width of the rectangle: "))
            height = int(input("Enter the height of the rectangle: "))
            color = input("Enter the color for the rectangle: ")
            draw_rectangle(width, height, color)
        else:
            print("Invalid input. Please enter a number between 0 and 4.")
            continue
        
        turtle.penup()
        turtle.goto(0, 0)  # Reset the position for the next drawing
        turtle.pendown()
        
        draw_more = input("Would you like to draw another shape (yes/no)? ")
        if draw_more.lower() != "yes":
            break
    
    turtle.done()
    print("Goodbye!")

if __name__ == "__main__":
    main()