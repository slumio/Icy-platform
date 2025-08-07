from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class HeuristicScores(BaseModel):
    """
    Data model for the calculated, heuristic-based scores for an influencer.
    This structure holds the output of the scoring_service.
    """
    brand_fit_score: float = Field(
        ..., 
        description="Overall compatibility score (0-100), representing the final weighted recommendation."
    )
    authenticity_score: float = Field(
        ..., 
        description="A score from 0-100 indicating how organic vs. polished the influencer's content feels."
    )
    audience_match_score: float = Field(
        ..., 
        description="A score from 0-100 representing the demographic and interest overlap with the brand's target audience."
    )
    engagement_quality: str = Field(
        ..., 
        description="A qualitative assessment of engagement ('High', 'Average', 'Low') based on heuristic rules."
    )

class Influencer(BaseModel):
    """
    The primary data model representing a single influencer.
    This structure is used to store data fetched from social media APIs
    and the results from our analysis.
    """
    handle: str = Field(
        ..., 
        description="The influencer's unique social media handle (e.g., '@handle')."
    )
    platform: str = Field(
        ..., 
        description="The platform where the influencer is active ('Instagram' or 'YouTube')."
    )
    followers: int = Field(
        ..., 
        description="The total number of followers the influencer has."
    )
    engagement_rate: float = Field(
        ..., 
        description="The influencer's average engagement rate as a percentage."
    )
    niche: List[str] = Field(
        ..., 
        description="A list of the influencer's primary content niches (e.g., 'beauty', 'sustainability')."
    )
    profile_pic_url: Optional[str] = Field(
        None, 
        description="A URL to the influencer's profile picture."
    )
    recent_posts: List[Dict] = Field(
        [], 
        description="A list of recent posts (dictionaries) used for AI analysis of content and tone."
    )
    scores: Optional[HeuristicScores] = Field(
        None, 
        description="The calculated heuristic scores for this influencer, populated after analysis."
    )