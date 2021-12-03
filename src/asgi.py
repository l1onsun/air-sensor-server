import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "hi hi v0.0.2"


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}


@app.get("/test")
def test(temp: float, co2: int, humi: int, date: float):
    date = date - 3600
    date = datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
    print(f"get date: {date}")
    print(f"get temp: {temp}")
    print(f"get co2: {co2}")
    print(f"get humi: {humi}")
