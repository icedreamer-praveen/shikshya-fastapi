from fastapi import FastAPI

from app.account.routers import accounts

from . import models
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(accounts.router)