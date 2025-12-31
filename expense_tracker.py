import json
from datetime import datetime
DATA_FILE = "data.json"

def load_expenses():
    try:
        with open(DATA_FILE,'r') as f:
            return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        return []
    
def save_expenses(total_expenses):
    with open(DATA_FILE,'w') as f:
        json.dump(total_expenses, f, indent=4)

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, etc): ")
    description = input("Enter description: ")
    expense ={
        'amount': amount,
        'category': category,
        'description': description,
        'date': datetime.now().strftime("%Y-%m-%d")
    }
    total_expenses = load_expenses()
    total_expenses.append(expense)
    save_expenses(total_expenses)
    print('✅ Expense added successfully!')

def view_expenses():
    total_expenses = load_expenses()
    if not total_expenses:
        print("No expenses found.")
        return
    for idx, exp in enumerate(total_expenses,start=1):
        print(
            f"{idx}. {exp['date']} | {exp['category']} | ₹{exp['amount']} | {exp['description']}"
            )
        
def category_summary():
    total_expenses = load_expenses()
    if not total_expenses:
        print("No expenses found.")
        return
    summary = {}

    for exp in total_expenses:
        category = exp['category']
        amount = exp['amount']
        summary[category] = summary.get(category, 0)+amount
        print("\n--- Category-wise Summary ---")

    for category, total in summary.items():
        print(f"{category} → ₹{total}")
    

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
