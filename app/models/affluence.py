from pydantic import BaseModel, Field
from typing import Dict, Optional
from datetime import date


class AffluenceScore(BaseModel):
    """Affluence Score model representing customer affluence level"""
    score: int = Field(ge=0, le=100, description="Affluence score (0-100)")

    def __int__(self):
        return self.score

    class Config:
        json_schema_extra = {
            "example": {
                "score": 86
            }
        }