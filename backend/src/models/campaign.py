from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from .influencer import Influencer

class BrandProfile(BaseModel):
    """
    Data model for the brand's setup information. This captures all the
    criteria the AI and heuristic engine will use for discovery.
    """
    product_details: str = Field(
        ..., 
        description="A detailed description of the brand's product or service."
    )
    target_audience: Dict = Field(
        ..., 
        description="Details of the target audience, e.g., {'age': [25, 35], 'interests': ['sustainability']}."
    )
    brand_tone: str = Field(
        ..., 
        description="The desired brand voice for outreach ('luxury', 'friendly', 'professional')."
    )
    budget: str = Field(
        ..., 
        description="The campaign's budget tier, which maps to influencer size ('micro', 'mid-tier', 'macro')."
    )
    niche: List[str] = Field(
        ..., 
        description="A list of the brand's primary niches to match with influencers."
    )

class Campaign(BaseModel):
    """
    The main data model for a marketing campaign. It ties together the user,
    the brand profile, and the results of the discovery process.
    """
    user_id: str = Field(
        ..., 
        description="The unique identifier of the user who created the campaign."
    )
    campaign_name: str = Field(
        ..., 
        description="The user-defined name for the campaign."
    )
    brand_profile: BrandProfile = Field(
        ..., 
        description="The detailed brand profile for this specific campaign."
    )
    discovered_influencers: List[Influencer] = Field(
        [], 
        description="A list of influencer objects that have been discovered and scored for this campaign."
    )
    status: str = Field(
        "draft", 
        description="The current status of the campaign ('draft', 'discovery_complete', 'active', 'completed')."
    )