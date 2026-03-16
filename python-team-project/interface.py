import logic


def menu():
    """
    Displays menu and processes user commands.
    """

    while True:
        print("\nTODO LIST MANAGER")
        print("1 - Show tasks")
        print("2 - Add task")
        print("3 - Delete task")
        print("4 - Search task")
        print("5 - Exit")

        choice = input("Choose option: ")

        if choice == "1":
            show_tasks()

        elif choice == "2":
            add_task()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            search_task()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


def show_tasks():
    tasks = logic.get()

    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def add_task():
    task = input("Enter new task: ")

    if logic.add(task):
        print("Task added.")
    else:
        print("Error adding task.")


def delete_task():
    task = input("Enter task to delete: ")

    if logic.delete(task):
        print("Task deleted.")
    else:
        print("Task not found.")


def search_task():
    keyword = input("Enter keyword: ")
    results = logic.search(keyword)

    if not results:
        print("No tasks found.")

    else:
        print("\nFound tasks:")
        for task in results:
            print("-", task)