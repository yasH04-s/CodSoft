def main():
    tasks = []

    while True:
        print("Welcome To To-Do List")
        print("1. Open the Lists")
        print("2. Add a task")
        print("3. Update a task")
        print("4. Mark task as done")
        print("5. (: Thank you :)")

        opt = input("Enter the option: ")

        if opt == '1':
            if not tasks:
                print("No tasks are available!")
            else:
                print("Tasks: ")
                for index, task in enumerate(tasks, start=1):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index}. {task['task']} - {status}")

        elif opt == '2':
            no_task = int(input("Enter the number of tasks to be added: "))
            for i in range(no_task):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added successfully!")

        elif opt == '3':
            task_index = int(input("Enter the task no. to update: ")) - 1
            if 0 <= task_index < len(tasks):
                new_task = input("Enter the updated task: ")
                tasks[task_index]["task"] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task no. ")

        elif opt == '4':
            task_index = int(input("Enter the task no. to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task no.")

        elif opt == '5':
            print("(: Thank you :)")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
