# PostgreSQL Students CRUD Application

This project implements a simple PostgreSQL database and a Python application that performs basic CRUD operations (Create, Read, Update, Delete) on a `students` table.

---

## ✅ Requirements
- PostgreSQL installed locally
- pgAdmin installed
- Python 3 installed

---

## 🗄️ Database Setup

1. Open pgAdmin and create a new database:
```sql
CREATE DATABASE schooldb;
Load the table structure:

sql
-- In pgAdmin Query Tool:
\i 'db/schema.sql'
Load the initial data:

sql
-- In pgAdmin Query Tool:
\i 'db/seed.sql'
Verify the inserted records:

sql
SELECT * FROM students ORDER BY student_id;
You should now see the 3 starter students.

💻 Running the Application (Windows)
Open PowerShell in your project folder:

powershell
cd C:\Users\okafo\OneDrive\Desktop\postgres-crud-students
Create and activate the virtual environment:

powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
Set PostgreSQL connection details:

powershell
$env:PGHOST="localhost"
$env:PGPORT="5432"
$env:PGDATABASE="schooldb"
$env:PGUSER="postgres"
$env:PGPASSWORD="1234"
Run the application:

powershell
python app\main.py
🎥 Video Demonstration
Watch the full CRUD demonstration here:
https://youtu.be/4DBuVmYXR98

📂 Project Structure
pgsql
postgres-crud-students/
│
├── app/
│   └── main.py
│
├── db/
│   ├── schema.sql
│   └── seed.sql
│
├── requirements.txt
└── README.md