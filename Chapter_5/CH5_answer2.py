num_list = []  
total_inputs = int(input("How many numbers do you want to analyze? "))

for i in range(total_inputs):  
    val = float(input(f"Enter value {i + 1}: "))  
    num_list.append(val)

if num_list:  
    print("
List Metrics Statistics:")  
    print("Sum:", sum(num_list))  
    print("Min:", min(num_list))  
    print("Max:", max(num_list))  
    print("Average:", sum(num_list) / len(num_list))
