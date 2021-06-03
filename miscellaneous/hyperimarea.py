# a simple python script to calculate hypotenuse, area and perimeter of a right triangle
from random import randint
from math import hypot

a, b =  randint(1,100), randint(1,100)

def find_hypotenuse(a, b):
    return hypot(a,b)

def find_area(a, b):
    return 0.5 * a * b

def find_perimeter(a, b):
    return a + b + find_hypotenuse(a, b)

def pprint():
    print(f"Calculating the area, hypotenuse and perimeter for a triangle with sides a:{a} and b:{b}!!")
    print(f"The hypotenuse is {round(find_hypotenuse(a, b), 2)} units")
    print(f"The area is {round(find_area(a, b), 2)} units\N{SUPERSCRIPT TWO}")
    print(f"The perimeter is {round(find_perimeter(a, b), 2)} units")

pprint()