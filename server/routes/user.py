from fastapi import APIRouter,Depends,HTTPException
from database import get_db
from sqlalchemy.orm import Session
from model import User,Order
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


@router.post('/insert')
def inserUserTable(db:Session=Depends(get_db)):
    name ="chintu"
    new_data =User(name =name)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return {
        "message":f"data added in name :{name}"
    }




@router.post('/insert/orders/{user_id}')
def insertOrders(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    newData = Order(
        product="mobile",
        user_id = user.id
    )

    db.add(newData)
    db.commit()
    db.refresh(newData)

    return {
        "user_id":user.id,
        "message":"order added"
    }

    
@router.get("/orders/{user_id}")
def getUser_order(user_id: int, db: Session = Depends(get_db)):

    user_orders = (
        db.query(User, Order)
        .join(Order, User.id == Order.user_id)
        .filter(User.id == user_id)
        .all()
    )

    if not user_orders:
        raise HTTPException(status_code=404, detail="User or orders not found")

    return {
        "user": {
            "id": user_orders[0][0].id,
            "name": user_orders[0][0].name
        },
        "orders": [
            {
                "id": order.id,
                "product": order.product
            }
            for user, order in user_orders
        ]
    }