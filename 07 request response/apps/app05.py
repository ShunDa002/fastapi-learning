from fastapi import APIRouter, File, UploadFile
from typing import List
import os

app05 = APIRouter()


# Suits for smaller file upload
@app05.post("/file")
async def get_file(file: bytes = File()):
    print(file, type(file))

    return {"file_size": len(file)}


@app05.post("/files")
async def get_files(files: List[bytes] = File()):
    for file in files:
        print(len(file))

    return {"total_file": len(files)}


@app05.post("/uploadfile")
async def get_uploadFile(file: UploadFile):
    print(file, type(file))

    base_dir = os.path.dirname(os.path.dirname(__file__))
    img_dir = os.path.join(base_dir, "imgs")
    os.makedirs(img_dir, exist_ok=True)
    path = os.path.join(img_dir, file.filename)
    # Save image
    with open(path, "wb") as f:
        for line in file.file:
            f.write(line)

    return {
        "file": file.filename,
    }


@app05.post("/uploadfiles")
async def get_uploadFiles(files: List[UploadFile]):
    print(files, type(files))

    return {
        "file": [file.filename for file in files],
    }
