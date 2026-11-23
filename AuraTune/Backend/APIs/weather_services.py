import httpx


BASE_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather_description(weather_code: int) -> str:
    """Convert Open-Meteo weather codes into readable descriptions."""

    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Light rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Light snow",
        73: "Moderate snow",
        75: "Heavy snow",
        77: "Snow grains",
        80: "Light rain showers",
        81: "Moderate rain showers",
        82: "Heavy rain showers",
        85: "Light snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Thunderstorm with heavy hail",
    }

    return weather_codes.get(weather_code, "Unknown weather")


async def get_weather(latitude: float, longitude: float):
    """Retrieve current weather from Open-Meteo."""

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "weather_code",
            "wind_speed_10m",
        ],
        "timezone": "auto",
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()

    current = data["current"]

    weather_code = current["weather_code"]

    return {
        "temperature": current["temperature_2m"],
        "feels_like": current["apparent_temperature"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "weather_code": weather_code,
        "weather_description": get_weather_description(weather_code),
        "timezone": data.get("timezone"),
    }
