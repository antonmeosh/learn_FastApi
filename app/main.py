from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def root():
    return FileResponse("public/index.html")


@app.post("/calculate")
def calculate(num1: int, num2: int):
    return f"result = {num1 + num2}"


@app.get("/custom")
def read_custom_message():
    return {"message": "Custom message"}
