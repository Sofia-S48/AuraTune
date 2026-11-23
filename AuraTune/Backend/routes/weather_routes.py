from fastapi import APIRouter
from APIs.weather_service import get_weather

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)


@router.get("/")
async def weather(latitude: float, longitude: float):
    return await get_weather(latitude, longitude)
