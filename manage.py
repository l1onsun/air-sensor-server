import subprocess  # nosec

from fire import Fire


def _run(*args: str):
    print(f">> {args}")
    subprocess.run(args)  # nosec


def run_debug():
    _run("uvicorn", "air_sensor.asgi:app")


def run_release():
    _run("uvicorn", "air_sensor.asgi:app")


def compile():
    _run("pip-compile")


def check():
    _run("pre-commit", "run", "-a")


if __name__ == "__main__":
    Fire()
