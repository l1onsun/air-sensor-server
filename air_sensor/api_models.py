from pydantic import BaseModel


class SensorData(BaseModel):
    temp: float
    co2: int
    humi: int
    date: float
