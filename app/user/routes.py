from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/create_user/", response_model=schemas.UserList)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router.get("/user-list/", response_model=list[schemas.UserList])
def user_list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db=db, skip=skip, limit=limit)

@router.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    if crud.delete_user(db=db, user_id=user_id):
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
