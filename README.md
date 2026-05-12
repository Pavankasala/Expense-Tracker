# 🚀 Expense Tracker API (FastAPI)

A **RESTful Expense Tracking & Analytics API** built using **Python and FastAPI**, designed with **clean architecture principles**.  
The application allows users to record expenses and retrieve **category-wise and monthly analytics** via HTTP endpoints.

This project demonstrates **backend development**, **API design**, **data aggregation**, and **modular Python architecture**.

---

## ✨ Features

### 📌 Core Functionality
- Add expenses via REST API
- Retrieve all stored expenses
- Delete expenses using a **unique ID**
- Persistent storage using JSON

### 📊 Analytics
- **Category-wise expense summary**
- **Monthly expense aggregation**
- Server-side computation of insights (not just CRUD)

### 🧱 Architecture
- Clean separation of concerns
- Modular and scalable project structure
- Easily extendable to SQLite / PostgreSQL

---

## 🗂 Project Structure

```text
Expense-Tracker/
├── app.py            # Application entry point
├── routes.py         # API routes
├── models.py         # Pydantic schemas
├── storage.py        # Data persistence layer
├── analytics.py      # Business & analytics logic
├── data.json         # Persistent storage
├── requirements.txt
└── README.md
```
---

## 🛠 Tech Stack

- **Language:** Python 3.13  
- **Framework:** FastAPI  
- **Server:** Uvicorn  
- **Validation:** Pydantic  
- **Storage:** JSON (file-based persistence)  

---

## 🚀 Getting Started
---
## 1️⃣ Clone the Repository
git clone https://github.com/Pavankasala/Expense-Tracker.git
cd Expense-Tracker

---

## 2️⃣ Install Dependencies
pip install -r requirements.txt

---

## 3️⃣ Run the Server
python -m uvicorn app:app --reload

---

## 4️⃣ Open API Docs
http://127.0.0.1:8000/docs

Interactive Swagger UI will be available.

---

## 🔌 API Endpoints

### ➕ Add Expense
POST /expenses

Request Body:
{
  "amount": 250,
  "category": "Food",
  "description": "Lunch"
}

---

### 📄 Get All Expenses
GET /expenses

---

### ❌ Delete Expense
DELETE /expenses/{expense_id}

---

### 📊 Category Analytics
GET /analytics/category

Response Example:
{
  "Food": 1200,
  "Travel": 800
}

---

### 📅 Monthly Analytics
GET /analytics/monthly

Response Example:
{
  "2025-01": 3200,
  "2025-02": 1800
}

---

## 🧠 Design Decisions
- Used UUID-based identifiers for safe and stable deletion
- Implemented clean architecture for readability and scalability
- Separated analytics logic for easier testing and maintenance
- Started with JSON persistence for simplicity, with clear upgrade paths

---

## 🔮 Future Enhancements
- Replace JSON with SQLite / PostgreSQL
- Add authentication (API Key / JWT)
- Export analytics to CSV
- Dockerize the application
- Add automated tests

---

## 👤 Author
Pavan Sai Kasala

GitHub: https://github.com/Pavankasala  
LinkedIn: https://www.linkedin.com/in/pavan-kasala-3499a8272  
Email: pavankasala999@gmail.com
