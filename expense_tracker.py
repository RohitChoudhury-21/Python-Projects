import os
import json
from datetime import datetime

expenses = []

def add_expense(expenses):
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense category (e.g., groceries, transportation, entertainment): ")
    description = input("Enter a brief description: ")
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    expenses.append({
        'date': date,
        'amount': amount,
        'category': category,
        'description': description
    })
    print("Expense added successfully!\n")

def list_expenses(expenses):
    if not expenses:
        print("No expenses recorded.\n")
    else:
        for expense in expenses:
            print(f"Date: {expense['date']}\nAmount: ${expense['amount']:.2f}\nCategory: {expense['category']}\nDescription: {expense['description']}\n")

def calculate_total_expenses(expenses, time_frame):
    total = 0
    for expense in expenses:
        expense_date = datetime.strptime(expense['date'], '%Y-%m-%d %H:%M:%S')
        if time_frame == 'daily' and expense_date.date() == datetime.now().date():
            total += expense['amount']
        elif time_frame == 'weekly' and (datetime.now() - expense_date).days < 7:
            total += expense['amount']
        elif time_frame == 'monthly' and expense_date.month == datetime.now().month:
            total += expense['amount']
    print(f"Total {time_frame} expenses: ${total:.2f}\n")

def generate_monthly_report(expenses):
    report = {}
    for expense in expenses:
        expense_date = datetime.strptime(expense['date'], '%Y-%m-%d %H:%M:%S')
        if expense_date.month == datetime.now().month:
            if expense['category'] in report:
                report[expense['category']] += expense['amount']
            else:
                report[expense['category']] = expense['amount']
    print("Monthly Report:")
    for category, total in report.items():
        print(f"Category: {category} - Total: ${total:.2f}")
    print()

def save_expenses(expenses, filename='expenses.json'):
    with open(filename, 'w') as file:
        json.dump(expenses, file)
    print("Expenses saved successfully!\n")

def load_expenses(filename='expenses.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def main():
    expenses = load_expenses()
    while True:
        print("Expense Tracker Application")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Calculate Total Expenses")
        print("4. Generate Monthly Report")
        print("5. Save Expenses")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            list_expenses(expenses)
        elif choice == '3':
            time_frame = input("Enter time frame (daily, weekly, monthly): ").strip().lower()
            calculate_total_expenses(expenses, time_frame)
        elif choice == '4':
            generate_monthly_report(expenses)
        elif choice == '5':
            save_expenses(expenses)
        elif choice == '6':
            save_expenses(expenses)
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
