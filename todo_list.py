import os
import json

tasks = []

def add_task(tasks):
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    task_id = len(tasks) + 1
    tasks.append({
        'id': task_id,
        'title': title,
        'description': description,
        'completed': False
    })
    print("Task added successfully!\n")

def list_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
    else:
        for task in tasks:
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"ID: {task['id']}\nTitle: {task['title']}\nDescription: {task['description']}\nStatus: {status}\n")

def mark_task(tasks):
    task_id = int(input("Enter the task ID to mark as complete/incomplete: "))
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            status = "completed" if task['completed'] else "incomplete"
            print(f"Task {task_id} marked as {status}.\n")
            break
    else:
        print("Task not found.\n")

def delete_task(tasks):
    task_id = int(input("Enter the task ID to delete: "))
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            print(f"Task {task_id} deleted successfully.\n")
            break
    else:
        print("Task not found.\n")

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file)
    print("Tasks saved successfully!\n")

def load_tasks(filename='tasks.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def main():
    tasks = load_tasks()
    while True:
        print("To-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete/Incomplete")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            mark_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
