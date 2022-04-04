from app.endpoints import create_users_endpoint, get_users_endpoint
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

def create_app():
    app = FastAPI()
    app.include_router(get_users_endpoint.router)
    app.include_router(create_users_endpoint.router)
    return app