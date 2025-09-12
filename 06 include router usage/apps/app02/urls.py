from fastapi import APIRouter

user = APIRouter()

@user.get("/login")
async def user_login():
    return {"user": "login"}

@user.get("/register")
async def user_register():
    return {"user": "register"}