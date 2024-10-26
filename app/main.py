from fastapi import FastAPI
from app.user.routes import router as user_router

#from store.routes import router as store_router
from .database import engine, Base


app = FastAPI()


Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(user_router, prefix="/users", tags=["Users"])
#app.include_router(store_router, prefix="/stores", tags=["Stores"])

# # Root route
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the API!"}
