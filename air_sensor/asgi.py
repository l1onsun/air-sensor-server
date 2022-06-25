import logging

from fastapi import Depends, FastAPI

from air_sensor.api_models import SensorData
from air_sensor.prometheus import observe_data, prometheus_asgi_app

log = logging.getLogger(__name__)

app = FastAPI()
app.mount("/metrics", prometheus_asgi_app)


@app.get("/sensor")
def test(data: SensorData = Depends()):
    log.debug(f"received: {data}")
    observe_data(data)
