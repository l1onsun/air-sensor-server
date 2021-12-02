from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "hi hi v0.0.2"

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}