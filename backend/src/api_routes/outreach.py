from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
import logging
from ..services.ai_service import AIService

# Create a router for outreach-related endpoints
router = APIRouter()

# --- Pydantic Model for Request Body ---

class OutreachRequest(BaseModel):
    """Defines the data structure required to generate an outreach message."""
    influencer_name: str = Field(..., description="The first name of the influencer.")
    brand_name: str = Field(..., description="The name of the brand conducting the outreach.")
    recent_post_topic: str = Field(..., description="A topic from one of the influencer's recent posts.")
    brand_tone: str = Field(..., description="The desired tone for the message (e.g., 'friendly', 'professional').")

# --- API Endpoint ---

@router.post("/generate-message", status_code=status.HTTP_200_OK)
async def generate_outreach_message(request: OutreachRequest):
    """
    Generates a personalized outreach message using the AI service.
    
    This endpoint takes structured data from the frontend, uses it to construct
    a detailed prompt, and gets a ready-to-send message from the AI model.
    """
    try:
        logging.info(f"Generating outreach message for influencer: {request.influencer_name}")
        
        # Delegate the core logic to the AIService
        message = AIService.generate_outreach_message(
            influencer_name=request.influencer_name,
            brand_name=request.brand_name,
            recent_post_topic=request.recent_post_topic,
            brand_tone=request.brand_tone
        )
        
        return {"message": message}
        
    except Exception as e:
        logging.error(f"Failed to generate outreach message: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while generating the message."
        )