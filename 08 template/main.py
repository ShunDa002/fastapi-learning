from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

base_dir = os.path.dirname(__file__)
template_dir = os.path.join(base_dir, "templates")
# print("Template Directory:", template_dir)
templates = Jinja2Templates(directory=template_dir)

## Access by: http://127.0.0.1:8080/index
@app.get("/index")
async def read_index(request: Request):
    name = "root"
    age = 24

    books = [
        {"title": "chainsaw man", "price": 19},
        {"title": "jujutsu kaisen", "price": 20},
        {"title": "dandadan", "price": 30},
        {"title": "kimetsu no yaiba", "price": 29},
    ]

    info = {"name": "eren yeager", "age": 24, "gender": "male"}

    pie = 3.1415926

    movies = {
        "adult": ["john wick", "inception", "interstellar"],
        "children": ["toy story", "frozen", "dispicable me"],
    }

    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": request,  # Necessary to pass Request object
            "user": name,
            "age": age,
            "books": books,
            "info": info,
            "pie": pie,
            "movies": movies,
        },
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
