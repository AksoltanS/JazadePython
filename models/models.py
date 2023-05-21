from sqlalchemy import Column, Integer, String, DateTime , ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime


class Department(Base):
    __tablename__  = 'department'
    id             = Column(Integer, primary_key=True, index=True)
    name           = Column(String, nullable=False)
    create_at      = Column(DateTime, default=datetime.now)
    update_at      = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    
class Employee(Base):
    __tablename__ = 'employee'
    id            = Column(Integer, primary_key=True, index=True)
    first_name    = Column(String, nullable=False)
    last_name     = Column(String, nullable=False) 
    department_id =Column( Integer, ForeignKey('department.id'))
    create_at     = Column(DateTime, default=datetime.now)
    update_at     = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    department = relationship('Department', back_populates='emloyee')