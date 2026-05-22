import csv

# Function to add expense
def add_expense():
    desc = input("Enter expense description: ")
    amount = input("Enter amount: ")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([desc, amount])

    print("Expense Added Successfully!")


# Function to view expenses
def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            print("\n----- All Expenses -----")

            for row in reader:
                print(f"Item: {row[0]} | Amount: ₹{row[1]}")

    except FileNotFoundError:
        print("No expenses found!")


# Function to calculate total expenses
def total_expenses():
    total = 0

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                total += int(row[1])

        print(f"\nTotal Expenses: ₹{total}")

    except FileNotFoundError:
        print("No expense file found!")


# Main menu function
def menu():

    while True:

        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice! Please try again.")


# Run the program
menu()
6
