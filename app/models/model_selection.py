from pydantic import BaseModel, Field
from typing import Dict, Optional
from datetime import date


class ScoreRequest(BaseModel):
    """Request model for the scoring API"""
    Id: int = Field(description="Unique identifier")
    customer_id: int = Field(description="EQX customer ID")
    bureau_path: str = Field(description="S3 path to bureau data")
    bureau_type: str = Field(default="CRIF", description="Bureau type (hardcoded as CRIF)")
    end_user: str = Field(default="1", description="End user identifier (hardcoded)")
    Create_date: date = Field(description="Creation date")

    class Config:
        json_schema_extra = {
            "example": {
                "Id": 123,
                "customer_id": 2345,
                "bureau_path": "s3://bucket/path/to/bureau/data.json",
                "bureau_type": "CRIF",
                "end_user": "1",
                "Create_date": "2024-01-15"
            }
        }


class ScoreResponse(BaseModel):
    """Response model for the scoring API"""
    Id: int
    customer_id: int
    Propensity_score: Dict[str, int]
    Affluence_score: int
    Intent_score: Dict[str, int]

    class Config:
        json_schema_extra = {
            "example": {
                "Id": 123,
                "customer_id": 2345,
                "Propensity_score": {
                    "PL": 1,
                    "CC": 1,
                    "LAMF": 1,
                    "CCBP": 1,
                    "CHR": 0,
                    "Digital Gold": 0,
                    "Insurance": 1
                },
                "Affluence_score": 86,
                "Intent_score": {
                    "PL": 97,
                    "CC": 22,
                    "LAMF": 1,
                    "CCBP": 1,
                    "CHR": 0,
                    "Digital Gold": 0
                }
            }
        }

