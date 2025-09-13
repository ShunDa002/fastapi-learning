from fastapi import FastAPI
import uvicorn
from apps.app01 import app01
from apps.app02 import app02
from apps.app03 import app03
from apps.app04 import app04
from apps.app05 import app05
from apps.app06 import app06
from fastapi.staticfiles import StaticFiles
import os
from apps.app07 import app07

app = FastAPI()

## Static docs request
## To access the file:
#     http://127.0.0.1:8080/static/css/common.css
base_dir = os.path.dirname(__file__)
static_dir = os.path.join(base_dir, "staticpages")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

app.include_router(app01, tags=["01 Path params"])
app.include_router(app02, tags=["02 Query params"])
app.include_router(app03, tags=["03 Request body params"])
app.include_router(app04, tags=["04 Form data (urlencoded)"])
app.include_router(app05, tags=["05 File upload"])
app.include_router(app06, tags=["06 Request.metadata"])
app.include_router(app07, tags=["07 Response model"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
