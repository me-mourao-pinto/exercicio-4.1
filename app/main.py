from fastapi import FastAPI

app = FastAPI(title="Exercício 4.1")


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
