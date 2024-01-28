import math ###imports math function
cyl_diam = float(input("What is the diameter of your cylinder in cm? ")) ###gives value to diameter
cyl_height = float(input("What is the heght of your cylinder in cm? ")) ###gives value to height
pi = round(3.141592 , 2) ###defines pi to 2 dec places
cyl_radius = cyl_diam / 2 ### converts cylinder diameter to radius
cyl_vol = pi * cyl_radius**2 * cyl_height ###cylinder volume formula
print(f"With your givden dimensions, the volume of the cylinder is {cyl_vol: .2f}cm^3") ###prints cylinder volume to user
