#  TO-DO LIST

todo_list = []

def show_tasks():
    if not todo_list:
        print("No tasks to show.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print("Task added.")

def delete_task():
    show_tasks()
    if not todo_list:
        return

    task_num = input("Enter the task number to delete: ")

    if task_num.isdigit():
        task_num = int(task_num)
        if 1 <= task_num <= len(todo_list):
            todo_list.pop(task_num - 1)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    else:
        print("Invalid input. Please enter a valid number.")

def main():
    while True:
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


main()
