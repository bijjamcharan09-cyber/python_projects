def display_menu(): #This function displays the main menu options to the user.
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")


def add_task(tasks): #This function prompts the user to enter a new task and adds it to the list of tasks.
    task = input("Enter a new task: ").strip().capitalize()

    if task == "":
        print("Task cannot be empty.")
        return

    tasks.append(task)
    print("Task added successfully.")


def view_tasks(tasks): #This function displays all the tasks in the list.
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n----- YOUR TASKS -----")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def main(): #This is the main function that runs the program, displaying the menu and handling user input.
    tasks = []

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            print("Thank you for using To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()