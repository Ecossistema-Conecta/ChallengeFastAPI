from app.routers import challenge, feedback
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.include_router(challenge.router)
app.include_router(feedback.router)
app.mount("/static", StaticFiles(directory="app/static", html=True), name="static")
