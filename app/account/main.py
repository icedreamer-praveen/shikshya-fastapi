from fastapi import FastAPI
from . import models
from .database import engine
from app.account.routers import accounts

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(accounts.router)