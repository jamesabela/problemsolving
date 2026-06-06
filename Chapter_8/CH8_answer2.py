import turtle  
import time

def flashing_timer(seconds):  
    print(f"Timer started for {seconds} seconds...")  
    time.sleep(seconds)  
      
    # Flash loop alternating canvas fill properties  
    for i in range(6):  
        if i % 2 == 0:  
            turtle.bgcolor("red")  
        else:  
            turtle.bgcolor("white")  
        time.sleep(0.5)

flashing_timer(3)  
turtle.done()
