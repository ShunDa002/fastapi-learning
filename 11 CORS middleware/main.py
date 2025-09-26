from fastapi import FastAPI, Request
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# @app.middleware("http")
# async def MyCORSMiddleware(request: Request, call_next):
#     response = await call_next(request)
#     response.headers["Access-Control-Allow-Origin"] = "*"         # *: allow all origins
#     return response

origins = [
    "*",
    ## list the rest of allowed origins here
    # "http://localhost:8000",
    ## ....
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/user")
async def get_user():
    print("user: meow meow")
    return {"user": "meow meow"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
