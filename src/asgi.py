import datetime
import sqlite3 as sql

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

    with sql.connect("database.db") as con:
        cur = con.cursor()

        cur.execute(""" CREATE TABLE IF NOT EXISTS info (
            date TEXT NOT NULL
            temp REAL 
            co2 INT
            humi INT        
            )""")
        cur.execute(""" INSERT INTO info VALUES(?,?,?,?)""", (str(date),temp,co2,humi))
    con.close()
