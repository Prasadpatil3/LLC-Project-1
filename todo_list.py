import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task_name = input("Enter task: ")
    task = {"task": task_name, "status": "Pending"}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
        return

    print("\n===== TASK LIST =====")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} [{task['status']}]")
    print()


def complete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["status"] = "Completed"
            save_tasks(tasks)
            print("Task marked as completed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input.\n")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{deleted['task']}' deleted.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input.\n")


def filter_tasks(tasks):
    print("1. View Pending Tasks")
    print("2. View Completed Tasks")
    choice = input("Enter choice: ")

    if choice == "1":
        print("\n--- Pending Tasks ---")
        for t in tasks:
            if t["status"] == "Pending":
                print("-", t["task"])
    elif choice == "2":
        print("\n--- Completed Tasks ---")
        for t in tasks:
            if t["status"] == "Completed":
                print("-", t["task"])
    else:
        print("Invalid choice")
    print()


def menu():
    tasks = load_tasks()

    while True:
        print("========== SMART TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Filter Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            filter_tasks(tasks)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    menu()