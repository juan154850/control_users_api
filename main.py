from fastapi import FastAPI
from router.router import user
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(user)
