"""
Personalisation Service Routes
"""
from fastapi import APIRouter, HTTPException
from typing import Dict
import logging

from app.models.model_selection import ScoreRequest, ScoreResponse
from app.services.propensity import PropensityScoreCalculator
from app.services.affluence import AffluenceScoreCalculator
from app.services.intent import IntentScoreCalculator

logger = logging.getLogger(__name__)

# Create router
router = APIRouter(prefix="/product-personalisation", tags=["scores"])

# Initialize service calculators
propensity_calculator = PropensityScoreCalculator()
affluence_calculator = AffluenceScoreCalculator()
intent_calculator = IntentScoreCalculator()


@router.post("/v1/model-scores", response_model=ScoreResponse)
async def calculate_scores(request: ScoreRequest) -> ScoreResponse:
    """
    Calculate Propensity, Affluence, and Intent scores for a customer
    
    Request Body:
    - Id: Unique identifier
    - customer_id: EQX customer ID
    - bureau_path: S3 path to bureau data
    - bureau_type: Bureau type (default: "CRIF")
    - end_user: End user identifier (default: "1")
    - Create_date: Creation date
    
    Returns:
    - Id: Request ID
    - customer_id: Customer ID
    - Propensity_score: Dictionary with product propensity scores (0/1)
    - Affluence_score: Affluence score (0-100)
    - Intent_score: Dictionary with product intent scores (0-100)
    """
    try:
        logger.info(f"Processing score calculation request for customer_id: {request.customer_id}, Id: {request.Id}")
        
        # Validate bureau_type (should be CRIF for now)
        if request.bureau_type != "CRIF":
            logger.warning(f"Unsupported bureau_type: {request.bureau_type}, expected CRIF")
            # Note: Still processing, but logging the warning
        
        # Validate end_user (should be "1" for now)
        if request.end_user != "1":
            logger.warning(f"Unexpected end_user: {request.end_user}, expected 1")
        
        # Calculate all scores
        propensity = propensity_calculator.calculate(
            customer_id=request.customer_id,
            bureau_path=request.bureau_path
        )
        
        affluence = affluence_calculator.calculate(
            customer_id=request.customer_id,
            bureau_path=request.bureau_path
        )
        
        intent = intent_calculator.calculate(
            customer_id=request.customer_id,
            bureau_path=request.bureau_path
        )
        
        # Format response
        # Convert PropensityScore to dict with "Digital Gold" key (with space)
        propensity_dict = propensity.model_dump()
        propensity_dict["Digital Gold"] = propensity_dict.pop("Digital_Gold")
        
        # Convert IntentScore to dict with "Digital Gold" key (with space)
        intent_dict = intent.model_dump()
        intent_dict["Digital Gold"] = intent_dict.pop("Digital_Gold")
        
        response = ScoreResponse(
            Id=request.Id,
            customer_id=request.customer_id,
            Propensity_score=propensity_dict,
            Affluence_score=affluence.score,
            Intent_score=intent_dict
        )
        
        logger.info(f"Successfully calculated scores for customer_id: {request.customer_id}")
        return response
        
    except Exception as e:
        logger.error(f"Error calculating scores for customer_id: {request.customer_id}, error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error calculating scores: {str(e)}")
