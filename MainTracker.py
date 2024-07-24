import json
from datetime import datetime

DATA_FILE = 'expenses.json'

def initialize_data_file():
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        with open(DATA_FILE, 'w') as file:
            json.dump([], file)
            data = []
    return data

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

def add_expense():
    amount = float(input("Enter the amount: "))
    description = input("Enter the description: ")
    category = input("Enter the category (e.g., food, transportation, entertainment): ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expense = {
        "amount": amount,
        "description": description,
        "category": category,
        "date": date
    }
    return expense

def categorize_expenses(expenses):
    categorized = {}
    for expense in expenses:
        category = expense['category']
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(expense)
    return categorized

def display_summary(expenses):
    print("\nExpense Summary:")
    categorized = categorize_expenses(expenses)
    for category, items in categorized.items():
        total = sum(item['amount'] for item in items)
        print(f"Category: {category}, Total: {total}")


def main():
    expenses = initialize_data_file()
    while True:
        print("\n1. Add Expense\n2. View Summary\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            expense = add_expense()
            expenses.append(expense)
            save_data(expenses)
        elif choice == '2':
            display_summary(expenses)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
