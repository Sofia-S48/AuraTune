from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.weather_routes import router as weather_router

# Create the FastAPI application
app = FastAPI(
    title="AuraTune API",
    description="Backend API for the AuraTune music recommendation app",
    version="1.0.0"
)
app.include_router(weather_router)

# Allow requests from our iOS app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to AuraTune API!",
        "status": "running"
    }

# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "app": "AuraTune"
    }
    
    
# Weather api
@app.get("/weather")
async def weather(latitude: float, longitude: float):
    return await get_weather(latitude, longitude)
