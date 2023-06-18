import mimetypes
from fastapi import FastAPI
from fastapi.responses import FileResponse
 
app = FastAPI()
 
@app.get("/")
def root():
    return FileResponse("public/index.html", 
                        filename="mainpage.html", 
                        media_type="application/octet-stream")