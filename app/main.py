"""
Main FastAPI application for EQX Decision Engine Service
"""
from fastapi import FastAPI
import logging
import uvicorn
from app.routes import personalisationService
from app.config.constant import settings

# Configure logging
logging.basicConfig(level=getattr(logging, settings.LOG_LEVEL))
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title=settings.API_TITLE,
    description="Service for calculating Propensity, Affluence, and Intent scores",
    version=settings.API_VERSION
)

# Include routers
app.include_router(personalisationService.router)


@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "EQX Decision Engine Service is running"}


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":    
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
