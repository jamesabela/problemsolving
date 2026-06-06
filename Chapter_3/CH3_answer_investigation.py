import turtle

polygon_sides = int(input("Number of sides: "))

for i in range(polygon_sides):  
    turtle.forward(50)  
    turtle.right(360 / polygon_sides) # The turning angle formula

turtle.done()
