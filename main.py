from fastapi import FastAPI

from app.account import views
from app.federal import federal

from app.account import models
from app.account.database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(views.router)
app.include_router(federal.router)