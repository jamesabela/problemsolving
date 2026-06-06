import turtle

def draw_grid_axes():  
    turtle.speed(0)  
    # Draw Horizontal X Axis  
    turtle.penup()  
    turtle.goto(-300, 0)  
    turtle.pendown()  
    turtle.goto(300, 0)  
      
    # Draw Vertical Y Axis  
    turtle.penup()  
    turtle.goto(0, -300)  
    turtle.pendown()  
    turtle.goto(0, 300)  
      
    turtle.done()

draw_grid_axes()
