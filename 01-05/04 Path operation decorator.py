from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/get")
async def get_test():
    return {"method": "get"}

@app.post("/post")
async def post_test(item: dict):
    return {"method": "post"}

@app.put("/put")
async def put_test(item: dict):
    return {"method": "put"}

@app.delete("/delete")
async def delete_test(item: dict):
    return {"method": "delete"}

if __name__ == "__main__":
    uvicorn.run("04 Path operation decorator:app", port=8080, reload=True)