from pydantic import BaseModel, Field
from typing import Dict, Optional
from datetime import date


class IntentScore(BaseModel):
    """Intent Score model with product-specific intent scores"""
    PL: int = Field(ge=0, le=100, description="Personal Loan intent score")
    CC: int = Field(ge=0, le=100, description="Credit Card intent score")
    LAMF: int = Field(ge=0, le=100, description="LAMF intent score")
    CCBP: int = Field(ge=0, le=100, description="CCBP intent score")
    CHR: int = Field(ge=0, le=100, description="CHR intent score")
    Digital_Gold: int = Field(ge=0, le=100, description="Digital Gold intent score")

    class Config:
        json_schema_extra = {
            "example": {
                "PL": 97,
                "CC": 22,
                "LAMF": 1,
                "CCBP": 1,
                "CHR": 0,
                "Digital_Gold": 0
            }
        }