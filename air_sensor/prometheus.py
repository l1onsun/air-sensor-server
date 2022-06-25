from prometheus_client import Gauge, Info, make_asgi_app

from air_sensor.api_models import SensorData
from air_sensor.utils import convert_to_datetime

temperature_summary = Gauge("temperature", "Temperature in degrees Celsius")
co2_summary = Gauge("co2", "CO2 level")
humidity_summary = Gauge("humidity", "Humidity level")
time_info = Info("time", "Observation time from sensor")

prometheus_asgi_app = make_asgi_app()


def observe_data(data: SensorData):
    temperature_summary.set(data.temp)
    co2_summary.set(data.co2)
    humidity_summary.set(data.humi)
    time_info.info({"time": str(convert_to_datetime(data.date))})
