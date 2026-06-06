import turtle

def draw_pacman():  
    turtle.speed(3)  
    turtle.color("yellow")  
    turtle.begin_fill()  
    # Draw the main circular wedge body shape  
    turtle.circle(100, 300)   
    turtle.goto(turtle.position()[0], turtle.position()[1])  
    # Close off outline toward central point locus coordinate tracking  
    turtle.goto(0, 100)   
    turtle.end_fill()  
    turtle.done()

draw_pacman()
