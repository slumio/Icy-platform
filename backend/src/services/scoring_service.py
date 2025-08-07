from ..models.campaign import BrandProfile
from ..models.influencer import Influencer, HeuristicScores
from .ai_service import AIService
import logging

class ScoringService:
    """
    The heuristic engine for scoring influencers based on brand compatibility.
    This service combines raw data with business logic to produce actionable insights.
    """
    @staticmethod
    def calculate_scores(influencer: Influencer, brand: BrandProfile) -> HeuristicScores:
        """
        Calculates all heuristic scores for a given influencer and brand profile.
        This method is the heart of the platform's "intelligence".
        """
        logging.info(f"Calculating scores for influencer: {influencer.handle}")

        # --- Heuristic 1: Engagement Quality (Quality over Quantity) ---
        engagement_quality = "Low"
        if influencer.followers < 100000 and influencer.engagement_rate > 3.0:
            engagement_quality = "High"  # Prioritize micro-influencers with high engagement
        elif influencer.engagement_rate > 1.5:
            engagement_quality = "Average"

        # --- Heuristic 2: Niche & Audience Alignment ---
        # A simple but effective check for niche overlap.
        audience_match_score = 50.0
        if set(brand.niche) & set(influencer.niche): # Check for intersection between sets
             audience_match_score = 85.0 # Higher score for direct niche overlap

        # --- Heuristic 3: AI-Powered Content Analysis ---
        # Delegate to the AI service to analyze content for authenticity and sentiment.
        authenticity_score, avg_sentiment = AIService.analyze_content_for_heuristics(influencer.recent_posts)

        # --- Final Weighted Score Calculation ---
        # These weights can be adjusted to prioritize different factors.
        brand_fit_score = (
            (audience_match_score * 0.5) +  # Audience and niche match is most important.
            (authenticity_score * 0.3) +    # Authentic content is key.
            (avg_sentiment * 0.2)           # Positive sentiment is a good sign.
        )

        return HeuristicScores(
            brand_fit_score=round(brand_fit_score, 2),
            authenticity_score=round(authenticity_score, 2),
            audience_match_score=round(audience_match_score, 2),
            engagement_quality=engagement_quality,
        )