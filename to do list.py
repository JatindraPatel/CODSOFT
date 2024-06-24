tasks = []

def add_task(task_description):
    task = {"description": task_description, "done": False}
    tasks.append(task)

def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks found:")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done Yet"
            print(f"{index}. {task['description']} ({status})")

def mark_done(task_number):
    if 1 <= task_number <= len(tasks):
        task = tasks[task_number - 1]
        if not task["done"]:
            task["done"] = True
            print(f"Task '{task['description']}' marked as done!")
        else:
            print("Task is already marked as done.")
    else:
        print("Invalid Task Number.")

def delete_task(task_number):
    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        print(f"Task '{deleted_task['description']}' deleted successfully!")
    else:
        print("Invalid Task Number.")

while True:
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_description = input("Enter task description: ")
        add_task(task_description)
        print(f"Task '{task_description}' added successfully!")
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        task_number = int(input("Enter the task number to mark as done: "))
        mark_done(task_number)
    elif choice == "4":
        task_number = int(input("Enter the task number to delete: "))
        delete_task(task_number)
    elif choice == "5":
        print("GOOD BYE! Have A Great Day!")
        break
    else:
        print("Invalid choice! Please try again.")
