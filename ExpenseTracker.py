import datetime
import json

# Global expenses list
expenses = []

# Menu function
def menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter Expenses by Category")
    print("4. Exit")

# Add expense function
def add_expense():
    amount = float(input("Enter the amount: "))
    category = input("Enter the category (Food, Travel, etc.): ")
    description = input("Enter a short description: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }
    expenses.append(expense)
    print("Expense added successfully!")

# View expenses function
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print("\n--- Your Expenses ---")
    for expense in expenses:
        print(f"{expense['date']} | {expense['category']} | ${expense['amount']} - {expense['description']}")

# Filter expenses by category function
def filter_expenses_by_category():
    category = input("Enter the category to filter by: ")
    filtered_expenses = [e for e in expenses if e['category'].lower() == category.lower()]
    
    if not filtered_expenses:
        print("No expenses found for this category.")
        return

    print(f"\n--- Expenses in {category} ---")
    for expense in filtered_expenses:
        print(f"{expense['date']} | ${expense['amount']} - {expense['description']}")

# Save expenses to a file
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
    print("Expenses saved to expenses.json")

# Load expenses from a file
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            global expenses
            expenses = json.load(file)
        print("Expenses loaded successfully.")
    except FileNotFoundError:
        print("No previous data found.")

# Main function
def main():
    load_expenses()
    
    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses_by_category()
        elif choice == "4":
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
