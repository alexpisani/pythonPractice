# Lab8_apisani-2.py
# Alex Pisani
# June 30 2024
# a menu with functions that lets the user choose to find out the 
# area and perimeter of a rectangle or circle

import math

def cir_area(radius):
    """calculates area of a circle"""
    area1 = math.pi*(radius**2)
    print("The area is", area1)
def cir_circum(radius):
    """calculates the circumfrence of a circle"""
    circum = 2*math.pi*radius
    print("The circumfrence is",circum)
def rect_area(width,length):
    """calculates area of a rectangle"""
    area2 = width*length
    print("The area is", area2)
def rect_perim(width,length):
    """calculates the perimeter of a rectangle"""
    perim = (width + length) *2
    print("The perimeter is",perim)

menu = """
Please choose one of the following:
1: Area of a circle
2: Circumfrence of a circle
3: Area of a rectangle
4: Perimeter of a rectangle
5: Quit
"""

repeat = True
while repeat == True:
    choice = input(menu)
    if not choice.isdigit():
        print ("please select 1-5")
        continue
    choice = int(choice)
    if choice == 1:
        radius = float(input("Please enter the circle's radius: "))
        cir_area(radius)
    elif choice == 2:
        radius = float(input("Please enter the circle's radius: "))
        cir_circum(radius)
    elif choice == 3:
        width = float(input("Please enter the rectangles width: "))
        length = float(input("Please enter the rectangle's length: "))
        rect_area(width,length)
    elif choice == 4:
        width = float(input("Please enter the rectangles width: "))
        length = float(input("Please enter the rectangle's length: "))
        rect_perim(width,length)
    elif choice == 5:
        print("Goodbye")
        break
    else:
        print("That is not a valid entry, please select 1-5")