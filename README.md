# 🎓 College Event Registration System

A full-stack student event registration web application built using **Python**, **MySQL**, **HTML**, **CSS**, and **JavaScript**.

---

# 🛠 Required Software

Before running the application, ensure the following software is installed on your system:

### 1. Python

Download Python:

https://www.python.org/downloads/

Verify installation:
'''bash
python --version
'''
---

### 2. MySQL Server

Download MySQL Community Installer:

https://dev.mysql.com/downloads/installer/

During installation:

Remember your **root password**

---

### 3. MySQL Workbench

Download MySQL Workbench:

https://dev.mysql.com/downloads/workbench/

Used to manage databases visually.

---

### 4. Git

Download Git:

https://git-scm.com/download/win

Verify installation:
'''bash
git --version
'''
---

### 5. VS Code (Recommended)

Download Visual Studio Code:

https://code.visualstudio.com/

---

# 🚀 Getting Started

Follow these steps to run the application locally.

---

# 1️⃣ Clone the Repository

Open Command Prompt and run:

git clone https://github.com/Korat-Yug/college-event-registration-system.git

Move into project folder:

cd college-event-registration-system

---

# 2️⃣ Install Required Python Libraries

Run:
'''bash
pip install flask mysql-connector-python
'''
This installs backend dependencies required for the application.

---

# 3️⃣ Database Setup (MySQL)

Open **MySQL Workbench**

Create a new query and run:
'''sql
CREATE DATABASE IF NOT EXISTS college_events;

USE college_events;

CREATE TABLE registrations (
id INT AUTO_INCREMENT PRIMARY KEY,
full_name VARCHAR(100) NOT NULL,
event_name VARCHAR(100) NOT NULL,
timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
'''
Alternatively, run the provided setup file:
'''
SOURCE database.sql;
'''
---

# 4️⃣ Configure Database Connection

Inside project folder locate:

example_config.py

Rename it to:

config.py

Update database password:
'''python
DB_CONFIG = {
"host": "localhost",
"user": "root",
"password": "YOUR_MYSQL_PASSWORD",
"database": "college_events"
}
'''
Save the file.

---

# 5️⃣ Start Backend Server

Run:
'''bash
python app.py
'''
Server will start at:

http://127.0.0.1:5000

---

# 6️⃣ Open Application in Browser

Visit:

http://127.0.0.1:5000

Fill the registration form and submit.

Data will be stored in MySQL database.

---

# 📊 Verify Stored Data

Open MySQL Workbench and run:

SELECT * FROM college_events.registrations;

You should see submitted records.

---

# 📁 Project Structure

college-event-registration-system/

app.py → Flask backend server

example_config.py → Database configuration template

database.sql → Database setup script

README.md → Project documentation

/templates

index.html → Registration page UI

/static

style.css → Styling file

script.js → Frontend logic and API communication

---

# ⚙ How the Application Works

User fills registration form

↓

JavaScript sends POST request to Flask server

↓

Flask processes request

↓

Data stored inside MySQL database

↓

Success popup displayed to user

---