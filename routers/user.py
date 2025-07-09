from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, models
from fastapi import APIRouter, Depends, status
from ..repository import user
from ..database import get_db

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("/")
def create_user(request: schemas.User, db: Session = Depends(get_db)):
   return user.create(request,db)

@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)