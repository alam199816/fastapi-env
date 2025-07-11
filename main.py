from fastapi import FastAPI
import models
from .database import engine
from .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Welcome to the Blog API!"}




