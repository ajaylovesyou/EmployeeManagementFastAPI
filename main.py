from fastapi import FastAPI
from auth import router
from schemas import Emp, User, UpdateEmp
from database import SessionLocal, EmpTable , UserTable

app = FastAPI()
app.include_router(router)

# emps = []

# Add Emp to database: 
@app.post("/add-emp")
def add_emp(emp: Emp):

    db = SessionLocal()
    existing_emp = db.query(EmpTable).filter(
        EmpTable.id == emp.id
    ).first()

    if existing_emp:
        db.close()
        return {
            "message": "ID Already Exists"
        }

    new_emp = EmpTable(
        id=emp.id,
        name=emp.name,
        age=emp.age
    )

    db.add(new_emp)
    db.commit()
    db.close()

    return {
        "message": "Employee Added Successfully"
    }

# View all emplosy
@app.get("/view-emp")
def view_emp():

    db = SessionLocal()
    all_emps = db.query(EmpTable).all()

    result = []
    for emp in all_emps:
        result.append({
            "id": emp.id,
            "name": emp.name,
            "age": emp.age
        })

    db.close()
    return {

        "all_emps": result

    }

# Delete emp with id of the emploty
@app.delete("/delete-emp")
def delete_emp(id: int):

    db = SessionLocal()
    emp = db.query(EmpTable).filter(
        EmpTable.id == id

    ).first()

    if emp:
        db.delete(emp)
        db.commit()
        db.close()
        return {
            "message": "Employee Successfully Deleted"
        }
    db.close()
    return {
        "message": "Employee Not Found"
    }

# Update Emps: 
@app.put("/update-emp")
def update_emp(id: int, updated_emp: UpdateEmp):

    db = SessionLocal()
    emp = db.query(EmpTable).filter(
        EmpTable.id == id

    ).first()

    if emp:
        emp.name = updated_emp.name
        emp.age = updated_emp.age
        db.commit()
        result = {
            
            "id": emp.id,
            "name": emp.name,
            "age": emp.age
        }
        db.close()
        return {
            "message": "Employee Information Updated Successfully",
            "updated_emp": result
        }
    db.close()
    return {
        "message": "No Employee Found"
    }

# search the employee: 
@app.get("/search-emp")
def search_emp(id: int):
    db = SessionLocal()
    emp = db.query(EmpTable).filter(
        EmpTable.id == id
    ).first()

    if emp:
        result = {
            "id": emp.id,
            "name": emp.name,
            "age": emp.age
        }
        db.close()
        return {
            "message": "Employee Found",
            "emp": result
        }
    db.close()
    return {
        "message": "Employee Not Found"
    }