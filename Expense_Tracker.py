from datetime import datetime

def load_expenses(filename="expenses.txt"): #This function loads expenses from a file and returns them as a list of dictionaries.
    expenses = []

    try: #Try to open the file and read its contents. If the file does not exist, it will be created when saving expenses.
        with open(filename, "r") as file:
            for line in file:
               try: #Try to split each line into its components and convert the amount to a float. If the line is invalid, it will be skipped.
                    transaction, category, amount, date, time = line.strip().split(",")
                    expenses.append({
                        "transaction": transaction,
                        "category": category,
                        "amount": float(amount),
                        "date": date,
                        "time": time
                    })
               except ValueError: #Exception handling for invalid lines in th file.
                    print(f"Skipping invalid line in {filename}: {line.strip()}")

    except FileNotFoundError: #Exception handling for file not found.
        pass

    return expenses


def save_expenses(expenses, filename="expenses.txt"): #This function saves the expenses to a file. 
    try: #Try to open the file in write mode and write each expense as a line in the file. 
        with open(filename, "w") as file:
            for expense in expenses:
                 file.write(
                f"{expense['transaction']},{expense['category']},{expense['amount']},{expense['date']},{expense['time']}\n"
            )
    except IOError: #Exception handling for file write errors. 
        print("Error saving expenses.")
    
def add_expense(expenses): #This function adds a new expense to the list of expenses. 
    while True: #This loop will continue until the user enters a valid transaction type.
        transaction = input("Enter transaction type (Income/Expense): ").strip().capitalize()

        if transaction in ("Income", "Expense"):
            break

        print("Please enter either 'Income' or 'Expense'.")

    while True: #This loop will continue until the user enters a valid category.
        category = input("Enter category: ").strip().capitalize()

        if category:
            break

        print("Category cannot be empty.")

    while True: #This loop will continue until the user enters a valid amount.
        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid amount.")

    now = datetime.now()

    expenses.append({ 
        "transaction": transaction,
        "category": category,                     #This line adds the transaction type to the expense dictionary.
        "amount": amount,
        "date": now.strftime("%d-%m-%Y"),
        "time": now.strftime("%I:%M:%S %p")
    })

    print("-------------------------")
    print(f"{transaction} added successfully.") #Shows a message indicating that the transaction has been added successfully.
    print("-------------------------")


def view_expenses(expenses): #This function displays all the recorded expenses in a formatted manner. If there are no expenses, it informs the user accordingly.
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("\n--- All Expenses ---") #Shows all recorded expenses in a formatted manner.
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Transaction: {expense['transaction']}\n   Category: {expense['category']}\n   Amount: ₹{expense['amount']:.2f}\n   Date: {expense['date']}\n   Time: {expense['time']}")
    print()


def total_expenses(expenses): #This function calculates and displays the total amount of expenses recorded. 
    total = sum(
        expense["amount"]
        for expense in expenses 
        if expense["transaction"] == "expense" or expense["transaction"] == "Expense"
    )
    print(f"Total Expenses: ₹{total:.2f}\n")


def clear_expenses(expenses, filename="tracker.txt"): #This function clears all recorded expenses after confirming with the user.
    confirm = input("Are you sure? (yes/no): ").lower()

    for expense in expenses:
        if expense["transaction"] == "Expense" or expense["transaction"] == "Income":
            if confirm == "yes":
                expenses.clear()
                open(filename, "w").close()
                print("All expenses cleared!")
            else:
                print("Operation cancelled.")

def search_expense(expenses): #This function allows the user to search for expenses by category. 
    name = input("Enter category: ").lower()

    found = False

    for expense in expenses:
        if expense["category"].lower() == name:
            print(expense)
            found = True

    if not found:
        print("No expense found.")

def delete_expense(expenses): #This function allows the user to delete a specific expense by its index in the list. 
    view_expenses(expenses) #Function calling.

    try:
        index = int(input("Enter expense number: ")) - 1

        if 0 <= index < len(expenses):
            expenses.pop(index)
            save_expenses(expenses)
            print("Expense deleted.")
        else:
            print("Invalid number.")

    except ValueError:
        print("Enter a valid integer.")

def total_category_expenses(expenses): #This function calculates and displays the total expenses for each category.
    totals = {}

    for expense in expenses:
       cat = expense["category"]
       totals[cat] = totals.get(cat, 0) + expense["amount"]

    for cat, amt in totals.items():
        print(cat, amt)

def edit_expense(expenses): #This function allows the user to edit an existing expense by selecting it from the list and updating its details.
    if not expenses:
        print("No expenses to edit.\n")
        return

    view_expenses(expenses) #Function calling.

    try: #Editing an expense starts from here.
        index = int(input("Enter expense number to edit: ")) - 1

        if index < 0 or index >= len(expenses):
            print("Invalid expense number.\n")
            return

        print("\nLeave blank to keep the current value.")

        transaction = input(f"New transaction({expenses[index]['transaction']}): ").strip().capitalize()

        category = input(f"New category ({expenses[index]['category']}): ").strip().capitalize()

        amount = input(f"New amount (₹{expenses[index]['amount']:.2f}): ").strip().capitalize()

        if transaction:
            expenses[index]["transaction"] = transaction

        if category:
            expenses[index]["category"] = category

        if amount:
            try:
                amount = float(amount)
                if amount > 0:
                    expenses[index]["amount"] = amount
                else:
                    print("Amount must be greater than 0.")
            except ValueError:
                print("Invalid amount. Previous amount kept.")

        save_expenses(expenses)

        print("Expense updated successfully!\n")

    except ValueError:
        print("Please enter a valid number.\n")

def current_balance(expenses): #This function calculates and displays the current balance by summing up all income and subtracting all expenses.
    total_income = 0
    total_expense = 0

    for expense in expenses:
        if expense["transaction"] == "Income":
            total_income += expense["amount"]

        elif expense["transaction"] == "Expense":
            total_expense += expense["amount"]

    balance = total_income - total_expense

    print("\n------ Current Balance ------") #Shows the current balance in a formatted manner.
    print(f"Total Income   : ₹{total_income:.2f}")
    print(f"Total Expenses : ₹{total_expense:.2f}")
    print(f"Current Balance: ₹{balance:.2f}")
    print("="*15)

def main(): #Main function that serves as the entry point for the Expense Tracker application.
    expenses = load_expenses()

    continue_choice = "yes"
    print("="*15)
    print("Expense Tracker") #Formatting the title of the application.
    print("="*15)

    while continue_choice in ["yes", "y", "1"]:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Clear Expenses")
        print("5. Search Expense")
        print("6. Delete Expense")
        print("7. Edit Expense")
        print("8. Current Balance")
        print("9. Exit")

        choice = input("Choose an option (1-9): ")

        match choice:
            case "1":
                add_expense(expenses)
                save_expenses(expenses)
            case "2":
                view_expenses(expenses)
            case "3":
                total_expenses(expenses)
            case "4":
                clear_expenses(expenses)
            case "5":
                search_expense(expenses)
            case "6":
                delete_expense(expenses)
            case "7":
                edit_expense(expenses)
            case "8":
                current_balance(expenses)
            case "9":
                save_expenses(expenses)
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")
        continue_choice = input("Do you want to continue? (yes/no): ").lower()

if __name__ == "__main__": #Checks if the script is being run directly (not imported) and calls the main function. 
    try:
        main()
    except KeyboardInterrupt: #Exception handling.
        print("\nProgram interrupted.")
