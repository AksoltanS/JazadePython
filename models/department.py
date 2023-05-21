from sqlalchemy.orm import Session 
from models import departmentSchema
from db import get_db
import crud

department_router = APIRouter()

@department_router.post('/add-department')
def add_department(req: departmentSchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_department (req,db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result )
