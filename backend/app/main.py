"""
This file is the entry point for the FastAPI application.
It creates the FastAPI instance and includes the routers from the api module.
It also creates the database tables using the Base.metadata.create_all() method.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import properties, auth
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(properties.router)
app.include_router(auth.router)
