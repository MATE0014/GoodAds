from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.v1 import api_router  # make sure this path is correct

app = FastAPI(
    title="The Good Ads API",
)

app.mount("/app", StaticFiles(directory="app/static"), name="static")  # match the correct folder

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to The Good Ads API"}
