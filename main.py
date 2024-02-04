from fastapi import FastAPI
from starlette.responses import FileResponse

app = FastAPI()


@app.get("/")
def root():
    return FileResponse(
        "public/index.html",
        filename="mainpage.html",
        media_type="application/octet-stream",
    )


@app.get("/file", response_class=FileResponse)
def get_file():
    return "public/index.html"
