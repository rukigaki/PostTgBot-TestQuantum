from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import HTTPBasic, HTTPBasicCredentials


security = HTTPBasic()

app_login = APIRouter(prefix="/auth", tags=["Auth"])

@app_login.post("/login")
async def login(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {
        "message": "Welcome!",
        "username": credentials.username,
        "password": credentials.password
    }


