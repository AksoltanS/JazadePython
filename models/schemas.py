from pydantic import BaseModel

class departmentSchema(BaseModel):
    name: str
    
    
class emloyeeSchema(BaseModel):
    first_name: str      
    last_name: str        
    department_id: int
