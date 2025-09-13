from fastapi import APIRouter
from typing import Union, Optional

app02 = APIRouter()


@app02.get("/jobs/{kw}")
# If no default value(None) is given, the parameter will be treated as required
def get_jobs(kw: str, edu: Union[str, None] = None, exp: Optional[str] = None):
    return {"kw": kw, "edu": edu, "exp": exp}
