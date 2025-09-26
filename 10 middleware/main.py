from fastapi import FastAPI, Request
import uvicorn
from fastapi.responses import Response
import time

app = FastAPI()


## The middlewares that are defined bottom will be executed first.
@app.middleware("http")
async def m2(request: Request, call_next):
    ## Request can be modified by code here
    print("m2 request")
    response = await call_next(request)
    ## Response can be modified by code here
    response.headers["author"] = "meow"
    print("m2 response")
    return response


@app.middleware("http")
async def m1(request: Request, call_next):
    ## Request can be modified by code here
    print("m1 request")
    # Blocking access from certain IP addresses
    # if request.client.host in ["127.0.0.1"]:
    #     return Response(status_code=403, content="visit forbidden")

    # Blocking access to certain paths
    # if request.url.path in ["/user"]:
    #     return Response(status_code=403, content="visit forbidden")

    start_time = time.time()

    response = await call_next(request)
    ## Response can be modified by code here
    print("m1 response")
    end_time = time.time()
    response.headers["ProcessTime"] = str(end_time - start_time)
    return response


@app.get("/user")
async def get_user():
    print("get_user executed")
    time.sleep(3)
    return {"user": "MeowMeow"}


@app.get("/item/{item_id}")
async def get_item(item_id: int):
    print("get_item executed")
    time.sleep(2)
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
