from fastapi import FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM
from api.student import student_api


app = FastAPI()

app.include_router(student_api, prefix="/student", tags=["course enrollment api"])


register_tortoise(
    app=app,
    config=TORTOISE_ORM,
    # generate_schemas=True,
    # add_exception_handlers=True,
)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
