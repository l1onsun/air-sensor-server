from fire import Fire
import subprocess
import sys


def run():
    subprocess.run(["uvicorn", "src.asgi:app"])


if __name__ == "__main__":
    Fire()
