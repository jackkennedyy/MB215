import math

def are_balls_touching(ball1, ball2):
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2
    
    # Calculate distance between circles
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Check if the sum of the radii is greater than or equal to the distance
    touching = r1 + r2 >= distance
    
    # Prepare output
    output = f"Ball 1: Center = ({x1}, {y1}), Radius = {r1}\n"
    output += f"Ball 2: Center = ({x2}, {y2}), Radius = {r2}\n"
    output += f"Distance between circles: {distance}\n"
    output += "Result: The balls are touching." if touching else "Result: The balls are not touching."
    
    return output

# Sample dimensions
ball1 = (4, 4, 3)
ball2 = (10, 5, 4)

# Function execution
are_balls_touching(ball1, ball2)
