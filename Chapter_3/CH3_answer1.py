size = int(input("Pyramid Size: "))

for i in range(1, size + 1):  
    # Calculate spaces for alignment and 'x' characters for structure  
    spaces = " " * (size - i)  
    blocks = "x" * (2 * i - 1)  
    print(spaces + blocks)
