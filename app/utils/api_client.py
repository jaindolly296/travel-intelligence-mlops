import os

import requests

from dotenv import load_dotenv


load_dotenv()

BASE_URL = os.getenv(
    "API_URL",
    "https://travel-intelligence-mlops-1.onrender.com"
)


def predict_flight(data: dict):

    response = requests.post(
        f"{BASE_URL}/predict",
        json=data,
        timeout=60
    )

    response.raise_for_status()

    return response.json()


def predict_hotel(data: dict):

    response = requests.post(
        f"{BASE_URL}/predict/hotel",
        json=data,
        timeout=60
    )

    response.raise_for_status()

    return response.json()
