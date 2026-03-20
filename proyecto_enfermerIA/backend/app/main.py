from fastapi import FastAPI
from app.routes.evaluacion import router
from app.database import engine
from app.models.evaluacion_model import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="EnfermerIA API")

app.include_router(router)