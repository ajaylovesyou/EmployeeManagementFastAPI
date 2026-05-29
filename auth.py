# Registration : 
from fastapi import APIRouter
from database import SessionLocal, UserTable
from schemas import User

router = APIRouter()

# If new user then register heree bro : 
@router.post("/register")
def register(user: User):

    db = SessionLocal()
    existing_user = db.query(UserTable).filter(
        UserTable.username == user.username
    ).first()

    if existing_user:
        db.close()
        return {
            "message": "Username Already Exists"
        }

    new_user = UserTable(
        username=user.username,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.close()

    return {
        "message": "User Registered Successfully"
    }


# Login codee
@router.post("/login")
def login(user: User):

    db = SessionLocal()

    existing_user = db.query(UserTable).filter(
        UserTable.username == user.username
    ).first()
    if not existing_user:

        db.close()
        return {
            "message": "Invalid Username"
        }

    if existing_user.password != user.password:

        db.close()
        return {
            "message": "Invalid Password"
        }

    db.close()

    return {
        "message": "Login Successful"
    }