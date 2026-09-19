# 🎓 Student Management System

A full-featured Student Management System built with Django, featuring CRUD operations, search, and dashboard statistics.

![Django](https://img.shields.io/badge/Django-5.0-green)
![Python](https://img.shields.io/badge/Python-3.12-blue)

## ✨ Features

- ➕ Add new students with validation
- 📋 View all students in a responsive table
- 🔍 Search by name, roll number, or email
- 🎯 Filter by course
- ✏️ Update student details
- 🗑️ Delete with confirmation
- 📊 Dashboard with statistics
- 🏆 Auto grade calculation (A+, A, B, C, D, F)
- 👨‍💼 Django Admin panel integration

## 🛠️ Tech Stack

- **Backend:** Django 5.0, Python 3.12
- **Database:** SQLite
- **Frontend:** HTML5, Bootstrap 5
- **Tools:** Git, VS Code

## 🚀 Installation

```bash
git clone https://github.com/anishsaini-dev/students-management-system.git
cd students-management-system

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
