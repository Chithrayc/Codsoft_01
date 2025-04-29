def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. remove task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How may task you want to add: "))
            
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            if tasks:
                try:
                    task_number = int(input("Enter the task number to remove: ")) - 1
                    if 0 <= task_number < len(tasks):
                        removed_task = tasks.pop(task_number)
                        print(f"Task '{removed_task}' removed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks available to remove.")   

        elif choice == '5':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

