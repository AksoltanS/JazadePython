from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from models import Location, baseSchema
from db import get_db


location_router = APIRouter()

@location_router.post('/add-location')
def add_location(req: baseSchema, db: Session = Depends(get_db)):
    try:
        new_add = Location(**req.dict())
        db.add(new_add)
        db.commit()
        db.refresh(new_add)
        new_add = jsonable_encoder(new_add)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=new_add)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Что-то пошло не так!!')
        


@location_router.get('/get-location')
def get_location(db: Session = Depends(get_db)):
    try:
        result = jsonable_encoder(db.query(Location).all())
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Что-то пошло не так!!')
    