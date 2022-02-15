from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import router1, router2
from models import Base
from config import engine
from common import add_custom_errors, handle_cors


def create_app():
    Base.metadata.create_all(bind=engine)
    app = FastAPI()
    handle_cors(app)
    app.include_router(router1)
    app.include_router(router2)
    add_custom_errors(app)
    return app
