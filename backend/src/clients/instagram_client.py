import logging
import requests
from typing import List, Dict, Any
from ..config import settings # To get the access token

class InstagramClient:
    """
    A client for making live requests to the Instagram Graph API.
    """
    BASE_URL = "https://graph.facebook.com/v19.0"

    @staticmethod
    async def find_by_niche(niche: List[str]) -> List[Dict[str, Any]]:
        """
        Searches for Instagram influencers by querying the API.
        Note: The actual Instagram API does not have a direct "search by niche"
        endpoint for public users. This simulates a search using hashtags.
        """
        if not niche:
            return []
        
        # We'll use the first niche as the primary search query.
        query = niche[0]
        logging.info(f"Searching Instagram API for hashtag: #{query}")

        # This endpoint gets recent top media for a hashtag.
        url = f"{cls.BASE_URL}/ig_hashtag_search"
        params = {
            "user_id": "YOUR_INSTAGRAM_USER_ID", # You get this from Meta's platform
            "q": query,
            "access_token": settings.INSTAGRAM_ACCESS_TOKEN
        }

        try:
            response = requests.get(url)
            response.raise_for_status() # Raises an error for bad responses
            hashtag_id = response.json()["data"][0]["id"]

            # Now, get top media for that hashtag
            media_url = f"{cls.BASE_URL}/{hashtag_id}/top_media"
            media_params = {
                "user_id": "YOUR_INSTAGRAM_USER_ID",
                "fields": "id,media_type,like_count,comments_count,caption,user",
                "limit": 10, # Get top 10 posts
                "access_token": settings.INSTAGRAM_ACCESS_TOKEN
            }
            media_response = requests.get(media_url, params=media_params)
            media_response.raise_for_status()
            
            # This is a simplified transformation. You would need to process this
            # data to fit your Influencer model.
            live_data = media_response.json()["data"]
            logging.info(f"Found {len(live_data)} posts from live Instagram API.")
            
            # This part would require more logic to extract unique users and their stats.
            # For now, we return an empty list to show the API call structure.
            return []

        except requests.exceptions.RequestException as e:
            logging.error(f"Error calling Instagram API: {e}")
            return []