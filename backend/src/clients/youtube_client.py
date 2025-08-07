import logging
from typing import List, Dict, Any
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from ..config import settings

class YouTubeClient:
    """
    A client for making live requests to the YouTube Data API.
    """
    
    @staticmethod
    async def find_by_niche(niche: List[str]) -> List[Dict[str, Any]]:
        """
        Searches for YouTube channels by a query string (niche).
        """
        if not niche:
            return []
        
        query = " ".join(niche)
        logging.info(f"Searching YouTube API for query: '{query}'")

        try:
            # Build the YouTube service object
            youtube = build("youtube", "v3", developerKey=settings.YOUTUBE_API_KEY)

            # Call the search.list method to retrieve results
            search_response = youtube.search().list(
                q=query,
                part="snippet",
                type="channel",
                maxResults=10
            ).execute()

            # This would require more processing to get follower counts, etc.
            # and transform into the Influencer model format.
            live_data = search_response.get("items", [])
            logging.info(f"Found {len(live_data)} channels from live YouTube API.")
            return []

        except HttpError as e:
            logging.error(f"An HTTP error {e.resp.status} occurred: {e.content}")
            return []
        except Exception as e:
            logging.error(f"An error occurred with the YouTube client: {e}")
            return []