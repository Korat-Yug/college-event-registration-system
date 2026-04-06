# 🎓 College Event Registration System

Simple full-stack event registration web application built using a **Python Flask backend** and **MySQL database** with a modern HTML, CSS, and JavaScript frontend.

This application allows students to register for events like **Tech Fest**, **Cultural Events**, and **Workshops**, and stores registration data securely inside a MySQL database.

---

# 🛠 Required Software

Before running the application, ensure the following software is installed on your system:

MySQL Database
https://dev.mysql.com/downloads/installer/

MySQL Workbench
https://dev.mysql.com/downloads/workbench/

Python
https://www.python.org/downloads/

pip (comes with Python)

Verify installation:

```
python -m ensurepip --upgrade
```

Git
https://git-scm.com/download/win

VS Code (Recommended)
https://code.visualstudio.com/

---

# 🚀 Getting Started

Follow these steps to run the application locally.

---

# 1️⃣ Clone the Repository

Open Command Prompt and run:

```
git clone https://github.com/YOUR_USERNAME/college-event-registration-system.git
```

Navigate into project folder:

```
cd college-event-registration-system
```

---

# 2️⃣ Install Required Dependencies

Run:

```
pip install flask mysql-connector-python
```

---

# 3️⃣ Database Setup (MySQL)

Open **MySQL Workbench**

Create a new query and run:

```sql
CREATE DATABASE IF NOT EXISTS college_events;

USE college_events;

CREATE TABLE registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    event_name VARCHAR(100) NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

Alternatively, run the provided setup file:

```sql
SOURCE database.sql;
```

---

# 4️⃣ Configure Database Connection

Inside project folder locate:

```
example_config.py
```

Rename it to:

```
config.py
```

Then update your MySQL password inside the file:

```python
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_MYSQL_PASSWORD",
    "database": "college_events"
}
```

Save the file.

---

# 5️⃣ Start Backend Server

Run:

```
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

# 6️⃣ Open Application in Browser

Open:

```
http://127.0.0.1:5000
```

Fill the registration form and submit.

Data will be stored in the MySQL database.

---

# 📊 Verify Stored Data

Open MySQL Workbench and run:

```sql
SELECT * FROM college_events.registrations;
```

You should see submitted entries.

---

# 📁 Project Structure

```
college-event-registration-system/

static/
    style.css
    script.js

templates/
    index.html

app.py
database.sql
example_config.py
README.md
```

---

# ⚙ How the Application Works

```
User fills registration form
        ↓
Frontend sends POST request
        ↓
Flask backend receives request
        ↓
Data stored in MySQL database
        ↓
Success popup displayed
```

---