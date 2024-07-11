from fastapi import FastAPI
from .routes import Usuario

app = FastAPI()

app.include_router(Usuario.rotas)
