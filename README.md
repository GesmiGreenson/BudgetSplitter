# 💸 Budget Splitter

This is a full-stack **Money Splitter App** that helps users easily split group expenses.

## 📂 Project Structure
budget_splitter/
├── budget_backend/ # Django backend (API)
├── budget_frontend/ # React frontend (UI)
└── README.md

## 🚀 Features
- Add, edit, and delete expenses
- Calculate split amounts for each person
- Filter expenses person-wise
- Beautiful landing page with navigation
- Responsive UI

## 🔧 Tech Stack
- **Frontend:** React.js
- **Backend:** Django REST Framework
- **Database:** SQLite (can be upgraded)

## 📦 Setup Instructions

### Backend (Django)
```bash
cd budget_backend
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
### Frontend (React)
cd budget_frontend
npm install
npm start
