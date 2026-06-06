import turtle  
import random

def draw_changing_maze():  
    turtle.speed(0)  
    turtle.pensize(3)  
    for i in range(40):  
        # Dynamically randomize side growth increments slightly  
        length = (i * 10) + random.randint(-5, 5)  
        turtle.forward(length)  
        turtle.right(90)  
    turtle.done()

draw_changing_maze()
