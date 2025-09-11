from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def home():
    return {"user_id": "1234"}

@app.get("/shop")
async def shop():
    return {"shop": "Product info..."}

if __name__ == "__main__":
    uvicorn.run("03 fastapi quickstart:app", host="127.0.0.1", port=8080, reload=True)