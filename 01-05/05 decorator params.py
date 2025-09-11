from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get(
    "/items",
    tags=["This is items api"],
    summary="This is summary",
    description="This is description...",
    response_description="This is response description",
    deprecated=True,
)
async def get_test():
    return {"method": "get"}


if __name__ == "__main__":
    uvicorn.run("05 decorator params:app", port=8080, reload=True)
