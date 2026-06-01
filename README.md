# Employee Management System API

A RESTful Employee Management System built using FastAPI, SQLAlchemy, MySQL, and Pydantic.

This project provides complete Employee CRUD operations along with User Registration functionality and follows a modular project structure suitable for learning backend development and internship-level projects.

---

## 🚀 Features

### Employee Management

- Add Employee
- View All Employees
- Search Employee by ID
- Update Employee Details
- Delete Employee

### User Management

- User Registration
- Unique Username Validation

### Project Architecture

- FastAPI REST APIs
- SQLAlchemy ORM
- MySQL Database
- Pydantic Data Validation
- Environment Variables using .env
- Modular File Structure

---

## 🛠️ Technologies Used

- Python
- FastAPI
- SQLAlchemy
- MySQL
- Pydantic
- PyMySQL
- Python-Dotenv
- Uvicorn

---

## 📂 Project Structure

```text
EmployeeManagement/
│
├── main.py
├── auth.py
├── database.py
├── schemas.py
├── requirements.txt
├── .gitignore
├── .env
│
├── __pycache__/
├── venv/
└── .vscode/
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/ajaylovesyou/EmployeeManagement.git
cd EmployeeManagement
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### macOS / Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create MySQL Database

```sql
CREATE DATABASE emp_db;
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory.

```env
DATABASE_URL=mysql+pymysql://root:yourpassword@localhost/emp_db
```

### 6. Run Application

```bash
uvicorn main:app --reload
```

---

## 📌 API Endpoints

### Employee APIs

| Method | Endpoint | Description |
|----------|----------|----------|
| POST | /add-emp | Add Employee |
| GET | /view-emp | View Employees |
| GET | /search-emp | Search Employee by ID |
| PUT | /update-emp | Update Employee |
| DELETE | /delete-emp | Delete Employee |

### User APIs

| Method | Endpoint | Description |
|----------|----------|----------|
| POST | /register | Register User |

---

## 📖 API Documentation

After running the application:

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## 🔒 Security

This project uses environment variables to protect sensitive credentials.

Database credentials are stored in:

```text
.env
```

and are excluded from GitHub using:

```text
.gitignore
```

---

## 🎯 Learning Outcomes

This project demonstrates:

- REST API Development
- CRUD Operations
- Database Integration
- SQLAlchemy ORM
- FastAPI Routing
- Pydantic Validation
- Environment Variables
- Modular Backend Architecture
- Git & GitHub Workflow

---

## 👨‍💻 Author

### Ajay Kushwaha

GitHub: https://github.com/ajaylovesyou

---

## 📄 License

This project is created for educational and learning purposes.

---

## ⭐ Future Improvements

- User Login API
- Password Hashing using bcrypt
- JWT Authentication
- Role-Based Access Control
- Employee Ownership per User
- Docker Deployment
- Unit Testing
- Production Deployment

---

## 🎉 Project Status

✅ Completed

This project successfully implements Employee CRUD operations with MySQL database integration, SQLAlchemy ORM, FastAPI backend APIs, User Registration functionality, environment variable security, and modular project architecture.