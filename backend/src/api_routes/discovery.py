from fastapi import APIRouter, HTTPException, status
import logging
from ..services.scoring_service import ScoringService
from ..clients.instagram_client import InstagramClient
from ..clients.youtube_client import YouTubeClient
from ..models.influencer import Influencer
from .campaigns import db # Import the mock DB from the campaigns module

# Create a router for discovery-related endpoints
router = APIRouter()

@router.post("/campaigns/{campaign_id}/discover", status_code=status.HTTP_200_OK)
async def discover_and_analyze_influencers(campaign_id: str):
    """
    This is the core endpoint that triggers the discovery and analysis process.
    It orchestrates fetching, scoring, and saving influencers for a campaign.
    """
    if campaign_id not in db["campaigns"]:
        logging.error(f"Discovery failed: Campaign with ID {campaign_id} not found.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Campaign with ID {campaign_id} not found."
        )

    logging.info(f"Starting discovery process for campaign: {campaign_id}")
    campaign_data = db["campaigns"][campaign_id]
    brand_profile = campaign_data["brand_profile"]

    # --- Step 1: Find Potential Influencers ---
    # Call clients to get a raw list of candidates from different platforms.
    # The `await` keyword is used because these would be network calls in a real app.
    ig_candidates = await InstagramClient.find_by_niche(brand_profile["niche"])
    yt_candidates = await YouTubeClient.find_by_niche(brand_profile["niche"])
    all_candidates = ig_candidates + yt_candidates

    if not all_candidates:
        logging.warning(f"No potential influencers found for campaign {campaign_id}.")
        return {"message": "No potential influencers found for the specified niche."}

    # --- Step 2: Score Each Influencer with the Heuristic Engine ---
    scored_influencers = []
    for data in all_candidates:
        influencer = Influencer(**data)
        # Here, the heuristic engine from ScoringService is called
        influencer.scores = ScoringService.calculate_scores(influencer, brand_profile)
        scored_influencers.append(influencer)
    logging.info(f"Scored {len(scored_influencers)} influencers.")

    # --- Step 3: Sort by Brand Fit Score ---
    # The results are sorted to present the most relevant influencers first.
    scored_influencers.sort(key=lambda i: i.scores.brand_fit_score, reverse=True)

    # --- Step 4: Save Results and Update Status ---
    # The final, sorted list is saved back to our mock database.
    db["campaigns"][campaign_id]["discovered_influencers"] = [i.dict() for i in scored_influencers]
    db["campaigns"][campaign_id]["status"] = "discovery_complete"
    logging.info(f"Discovery for campaign {campaign_id} complete.")

    return {
        "message": "Discovery complete",
        "influencer_count": len(scored_influencers)
    }