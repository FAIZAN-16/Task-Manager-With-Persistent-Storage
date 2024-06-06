import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as file:
                tasks = [line.strip() for line in file]
        except IOError as e:
            print(f"Error reading tasks file: {e}")
    return tasks

def save_tasks(tasks):
    try:
        with open(TASKS_FILE, 'w') as file:
            for task in tasks:
                file.write(f"{task}\n")
    except IOError as e:
        print(f"Error writing to tasks file: {e}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
            save_tasks(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def update_task(tasks):
    list_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to update: "))
        if 0 < task_num <= len(tasks):
            new_task = input("Enter the new task description: ")
            tasks[task_num - 1] = new_task
            save_tasks(tasks)
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            update_task(tasks)
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
