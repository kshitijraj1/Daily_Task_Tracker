import os

# Initialize an empty list to store tasks
tasks = []

# Check if a task file exists and load tasks from it
task_file = "tasks.txt"
if os.path.exists(task_file):
    with open(task_file, "r") as file:
        tasks = [line.strip() for line in file.readlines()]

# Function to save tasks to a file
def save_tasks():
    with open(task_file, "w") as file:
        file.write("\n".join(tasks))

# Function to add a task
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("Tasks for the day:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to mark a task as completed
def complete_task():
    view_tasks()
    task_number = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number] = f"[Completed] {tasks[task_number]}"
        save_tasks()
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        deleted_task = tasks.pop(task_number)
        save_tasks()
        print(f"Task '{deleted_task}' deleted successfully!")
    else:
        print("Invalid task number.")

# Function to search and filter tasks
def search_and_filter():
    keyword = input("Enter a keyword to search/filter tasks: ").lower()
    filtered_tasks = [task for task in tasks if keyword in task.lower()]
    if not filtered_tasks:
        print("No matching tasks found.")
    else:
        print("Matching tasks:")
        for i, task in enumerate(filtered_tasks, 1):
            print(f"{i}. {task}")

# Function to display task details
def task_details():
    view_tasks()
    task_number = int(input("Enter the task number to view details: ")) - 1
    if 0 <= task_number < len(tasks):
        print(f"Task Details: {tasks[task_number]}")
    else:
        print("Invalid task number.")

# Function to handle errors and invalid input
def handle_error():
    print("Invalid choice. Please select a valid option.")

# Main loop
while True:
    print("\n===== Daily Task Tracker =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Search and Filter Tasks")
    print("6. Task Details")
    print("7. Task Count")
    print("8. Export Tasks")
    print("9. Import Tasks")
    print("10. Help")
    print("11. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        complete_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        search_and_filter()
    elif choice == '6':
        task_details()
    elif choice == '7':
        print(f"Total tasks: {len(tasks)}, Completed tasks: {tasks.count('[Completed]')}")
    elif choice == '8':
        with open("tasks_export.txt", "w") as file:
            file.write("\n".join(tasks))
        print("Tasks exported to 'tasks_export.txt'")
    elif choice == '9':
        try:
            with open("tasks_import.txt", "r") as file:
                imported_tasks = [line.strip() for line in file.readlines()]
            tasks.extend(imported_tasks)
            save_tasks()
            print("Tasks imported successfully!")
        except FileNotFoundError:
            print("No 'tasks_import.txt' file found.")
    elif choice == '10':
        print("===== Help =====")
        print("1. Add Task: Add a new task to your list.")
        print("2. View Tasks: Display your current task list.")
        print("3. Mark Task as Completed: Mark a task as completed.")
        print("4. Delete Task: Delete a task from the list.")
        print("5. Search and Filter Tasks: Find tasks containing a keyword.")
        print("6. Task Details: View details of a specific task.")
        print("7. Task Count: Display the total and completed task count.")
        print("8. Export Tasks: Export tasks to a file.")
        print("9. Import Tasks: Import tasks from a file.")
        print("11. Exit: Quit the Task Tracker.")
    elif choice == '11':
        save_tasks()
        print("Exiting the Task Tracker. Have a productive day!")
        break
    else:
        handle_error()
