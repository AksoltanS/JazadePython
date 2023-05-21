from fastapi import FastAPI
from db import Base, engine
from routers import location_router

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(location_router, tags=['Location'])
