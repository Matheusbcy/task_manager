loop = True
file_name = "gerenciador.txt"

while loop:
    print("Welcome to your task manager")
    print("1. Add new task: ")
    print("2. Which task did you complete? ")
    print("3. List pending tasks ")
    print("4. List completed tasks ")
    print("5. Exit")

    choice = input("Enter the option: ")

    if choice == "1":
        task = input("What is the name of the task?")
        completed_pending = input("The task is completed or pending? ").strip().lower()
        if completed_pending not in ["completed", "pending"]:
            print("Invalid status. Please enter 'completed' or 'pending'.\n")
            continue
        with open(file_name, "a") as file:
            file.write(f"{task}: {completed_pending}\n")
        print("Your task has been added to the manager\n")

    elif choice == "2":
        task_to_complete = input("What is the name of the task you completed? ")
        with open(file_name, "r") as file:
            tasks = file.readlines()
        found = False
        with open(file_name, "w") as file:
            for task in tasks:
                task_name, status = task.strip().split(":")
                if task_name == task_to_complete:
                    file.write(f"{task_name}: completed\n")
                    found = True
                else:
                    file.write(task)
        if found:
            print("Your task has been marked as completed\n")
        else:
            print("Task not found\n")
    elif choice == "3":
        print("Here is the list of pending tasks\n")
        with open(file_name, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_name, status = task.strip().split(": ")
                if status == "pending":
                    print(f"- {task_name}\n")
    elif choice == "4":
        print("Here is the list of completed tasks\n")
        with open(file_name, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_name, status = task.strip().split(": ")
                if status == "completed":
                    print(f"{task_name}\n")
    elif choice == "5":
        print("Exiting the program")
        loop = False
