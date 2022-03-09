from fastapi import FastAPI
from fastapi.logger import logger as fastapi_logger
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

if "CLIENT_URL" in os.environ:
    origins = [os.environ["CLIENT_URL"])]
else:
    # Local development URLs
    origins = [
        "http://localhost:8080",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fastapi_logger.info(f"CORS origins: {origins}")


@app.get("/weather")
async def weather():
    return [
        {
            "state": "AZ",
            "city": "Phoenix",
            "january": {"high": 60, "low": 45},
        },
        {
            "state": "MT",
            "city": "Bozeman",
            "january": {"high": 45, "low": 20},
        },
    ]
