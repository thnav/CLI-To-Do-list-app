todo_list = []

def menu_list():
    print("-- Chose a Option --")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks():
    if todo_list:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
        print()
    else:
        print("Your task list is empty")

def add_task():
    task = input("Enter a task : ")
    if task:
        todo_list.append(task)
        print(f"'{task}' Added!")
    else:
        print("Invalid task")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter the task number to remove"))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"'{removed}' is removed!")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a valid task number")

# Loop

while True:
    menu_list()
    choice = int(input("Choose an option(1-4) : "))
    if choice == 1:
        view_tasks()
    elif choice == 2:
        add_task()
    elif choice == 3:
        remove_task()
    elif choice == 4:
        print("Good bye!")
        break
    else:
        print(f"'{choice}' is not a valid option")