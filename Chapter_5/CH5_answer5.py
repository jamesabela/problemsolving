todo_list = []

while True:  
    print("
--- To-Do List Menu ---")  
    print("1. View Tasks")  
    print("2. Add Task")  
    print("3. Delete Task")  
    print("4. Exit")  
      
    choice = input("Select an option (1-4): ").strip()  
      
    if choice == "1":  
        if not todo_list:  
            print("Your to-do list is empty!")  
        else:  
            for i, task in enumerate(todo_list, 1):  
                print(f"{i}. {task}")  
    elif choice == "2":  
        new_task = input("Enter the new task: ").strip()  
        if new_task:  
            todo_list.append(new_task)  
            print(f"'{new_task}' added successfully.")  
    elif choice == "3":  
        if not todo_list:  
            print("Nothing to delete.")  
        else:  
            for i, task in enumerate(todo_list, 1):  
                print(f"{i}. {task}")  
            del_idx = int(input("Enter number of task to complete/remove: ")) - 1  
            if 0 <= del_idx < len(todo_list):  
                removed = todo_list.pop(del_idx)  
                print(f"Removed task: '{removed}'")  
            else:  
                print("Invalid task number.")  
    elif choice == "4":  
        print("Goodbye!")  
        break  
    else:  
        print("Invalid choice configuration option.")
