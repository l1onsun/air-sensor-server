from fire import Fire
import subprocess


def run():
    subprocess.run(["uvicorn", "src.asgi:app"])


if __name__ == "__main__":
    Fire()
