from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
import database, models
from schemas import UserCreate, UserUpdate, UserResponse

#Users
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=UserCreate, status_code=201)
def create_users(user: UserCreate, db: Session = Depends(database.get_db)):
    new_user = models.UserModel(name=user.name, email=user.email, age=user.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return(new_user)


@router.get("/", response_model=list[UserResponse], status_code=201)
def get_users(skip: int=0, limit: int = 10, db: Session = Depends(database.get_db)):
    users = db.query(models.UserModel).offset(skip).limit(limit).all()

    if not users:
        raise HTTPException(
            status_code=404,
            detail="User no found"
        )
    return users

@router.delete("/{user_id}", status_code=204)
def delete_users(id: int, db: Session = Depends(database.get_db)):
    delete_user = db.query(models.UserModel).filter(models.UserModel.id == id).first()
   
    if not delete_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    db.delete(delete_user)
    db.commit()