from fastapi import APIRouter, Request

app06 = APIRouter()


@app06.post("/items")
def get_user(request: Request):
    print("URL:", request.url)
    print("Clint IP:", request.client.host)
    print("Client info:", request.headers.get("user-agent"))

    return {
        "URL": request.url,
        "Client IP": request.client.host,
        "Client info": request.headers.get("user-agent"),
        "Cookies": request.cookies,
    }
