def create_checkerboard(n, m):  
    grid = []  
    for r in range(n):  
        row = []  
        for c in range(m):  
            # Alternating states logic checked using modulo of cumulative coordinates  
            if (r + c) % 2 == 0:  
                row.append(".")  
            else:  
                row.append("*")  
        grid.append(row)  
          
    for row in grid:  
        print("".join(row))

create_checkerboard(5, 5)
