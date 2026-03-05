# Hospital Management System

## About
**Hospital Management System** – A Python & MySQL project for managing doctors, patients, and users efficiently. Currently under development features a simple GUI built with Tkinter.

---

## Features
- Manage doctors (add, view, edit)
- Manage patients
- User registration and login system
- GUI interface with Tkinter
- Secure connection to MySQL database

*Note: Some features are still in progress.*

---

## Database
The database is built with MySQL.  
- Database name: `hms`  
- Tables:  
  - `hms_add_doctor`  
  - `hms_add_patient`  
  - `hms_user`  

**Important:** The actual database with data is not included. Use `schema.sql` to create the database locally.

---
**Installation & Run:**
```bash
    git clone https://github.com/<USERNAME>/Hospital-Management-System.git
    pip install mysql-connector-python
    pip install tk
