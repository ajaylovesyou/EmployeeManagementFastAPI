# database 
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os 

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class EmpTable(Base):

    __tablename__ = "emps"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    age = Column(Integer)


class UserTable(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True)
    password = Column(String(255))

Base.metadata.create_all(bind=engine)