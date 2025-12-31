from fastapi import APIRouter
from datetime import datetime
import uuid

from models import Expense
from storage import load_expenses, save_expenses
from analytics import category_analytics, monthly_analytics

router = APIRouter()

@router.post("/expenses")
def add_expense(expense: Expense):
    expenses = load_expenses()

    new_expense = {
        "id": uuid.uuid4().hex[:8],
        "amount": expense.amount,
        "category": expense.category,
        "description": expense.description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(new_expense)
    save_expenses(expenses)

    return new_expense

@router.get("/expenses")
def get_expenses():
    return load_expenses()

@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: str):
    expenses = load_expenses()

    for i, exp in enumerate(expenses):
        if exp["id"] == expense_id:
            deleted = expenses.pop(i)
            save_expenses(expenses)
            return deleted

    return {"error": "Expense not found"}

@router.get("/analytics/category")
def category_summary():
    return category_analytics(load_expenses())

@router.get("/analytics/monthly")
def monthly_summary():
    return monthly_analytics(load_expenses())
