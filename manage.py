import subprocess  # nosec

from fire import Fire


def run_debug():
    subprocess.run(["uvicorn", "air_sensor.asgi:app"])  # nosec


def run_release():
    subprocess.run(["uvicorn", "air_sensor.asgi:app"])  # nosec


if __name__ == "__main__":
    Fire()
