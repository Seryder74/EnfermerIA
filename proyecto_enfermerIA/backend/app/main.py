from fastapi import FastAPI
from app.routes.evaluacion import router

app = FastAPI(title="EnfermerIA API")

app.include_router(router)