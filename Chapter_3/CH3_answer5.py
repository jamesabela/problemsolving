# Iterative approach is much faster than recursion for computing up to 100 items  
fib_sequence = [0, 1]

for i in range(2, 100):  
    next_num = fib_sequence[-1] + fib_sequence[-2]  
    fib_sequence.append(next_num)

print("First 100 Fibonacci numbers:")  
for index, num in enumerate(fib_sequence, 1):  
    print(f"{index}: {num}")
