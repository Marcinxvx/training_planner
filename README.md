# Training Planner Django Project

---

# 🏋️‍♂️ Training Planner

A web application built with Django for creating and managing workout plans, sessions, and exercises.  
It also allows users to export workout plans to PDF and use an AI-powered assistant for training advice.  
The project was created for educational purposes during Django learning.

---

## 📌 Features

- Create and edit workout plans
- Add workout sessions to plans
- Create custom exercises
- Copy exercises from other users
- Assign exercises to sessions
- Generate a PDF version of the workout plan
- Search public exercise database
- OpenAI integration (AI Assistant) for personalized training advice
- User registration and login system
- Manage user-specific data

---

## ⚙️ Technologies Used

- Python 3.12+
- Django 5.2.4
- SQLite (default database)
- HTML + Django Templates
- WeasyPrint
- OpenAI Python SDK
- pytest + pytest-django
- python-dotenv

---

## 🧑‍💻 How to Run the Project Locally

```bash
git clone https://github.com/Marcinxvx/training_planner.git
cd training_planner
python -m venv venv
source venv/bin/activate  # (Linux/macOS) or venv\Scripts\activate (Windows)
pip install -r requirements.txt
```

---

## 🔐 Environment Variable Setup

To use the AI assistant feature, you must set your OpenAI API key.

1. Create a `.env` file in the project root.
2. Add the following line:

```env
OPENAI_API_KEY=your_api_key_here
```

You can get your API key from: https://platform.openai.com/account/api-keys

---

## 🧪 Running Tests

The project includes unit tests using `pytest`.

Run them with:

```bash
pytest
```

---

## 📄 License

This project is for educational use only — no formal license.
