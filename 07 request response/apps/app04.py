from fastapi import APIRouter, Form

app04 = APIRouter()


@app04.post("/reg")
async def register(username: str = Form(default=None), password: str = Form()):
    print(f"username: {username}, password: {password}")
    return {"username": username, "password": password}
