from fastapi import FastAPI
import uvicorn
from apps.app01.urls import shop
from apps.app02.urls import user

app = FastAPI()

app.include_router(shop, prefix="/shop", tags=["shop api"])
app.include_router(user, prefix="/user", tags=["user api"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)