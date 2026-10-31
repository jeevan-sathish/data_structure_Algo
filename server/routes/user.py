from fastapi import APIRouter,Depends,HTTPException
from database import get_db
from sqlalchemy.orm import Session
from model import User
from pydantic import BaseModel
from sqlalchemy.exc import SQLAlchemyError,IntegrityError


router = APIRouter(prefix ='/users')

@router.get('/')
def get_user(db:Session=Depends(get_db)):
    users = db.query(User).all()
    return users




class UserData(BaseModel):
    name:str
    age:int

class UserResponse(BaseModel):
    user :UserData


@router.post('/add' ,status_code =201)
def add_user(data:UserResponse,db:Session=Depends(get_db)):
   try:
        userData =User(
                   name =data.user.name,
                   age = data.user.age
               )
        db.add(userData)
        db.commit()
        db.refresh(userData)
        return {
                   "message":f"user:{data.user.name} age:{data.user.age} is added successfully"
               }
   except IntegrityError :
       db.rollback()
       raise HTTPException(
           status_code =409,
           detail="User already exist"
       )
   except SQLAlchemyError :
       raise HTTPException(
           status_code =500,
           detail="Database operation failed"
       )
