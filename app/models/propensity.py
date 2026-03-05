from pydantic import BaseModel, Field
from typing import Dict, Optional
from datetime import date


class PropensityScore(BaseModel):
    """Propensity Score model with product-specific scores (0 or 1)"""
    PL: int = Field(ge=0, le=1, description="Personal Loan propensity")
    CC: int = Field(ge=0, le=1, description="Credit Card propensity")
    LAMF: int = Field(ge=0, le=1, description="LAMF propensity")
    CCBP: int = Field(ge=0, le=1, description="CCBP propensity")
    CHR: int = Field(ge=0, le=1, description="CHR propensity")
    Digital_Gold: int = Field(ge=0, le=1, description="Digital Gold propensity")
    Insurance: int = Field(ge=0, le=1, description="Insurance propensity")

    class Config:
        json_schema_extra = {
            "example": {
                "PL": 1,
                "CC": 1,
                "LAMF": 1,
                "CCBP": 1,
                "CHR": 0,
                "Digital_Gold": 0,
                "Insurance": 1
            }
        }
