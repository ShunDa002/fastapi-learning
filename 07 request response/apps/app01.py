from fastapi import APIRouter

app01 = APIRouter()


# Path has an order, 1st declared path will be matched first, so put specific path first
# root user
@app01.get("/user/1")
def get_user():
    return {"user_id": "root user"}


@app01.get("/user/{id}")
def get_user(id):
    print("id", id, type(id))
    return {"user_id": id}


@app01.get("/articles/{id}")
def get_article(id: int):
    print("id", id, type(id))
    return {"article_id": id}
