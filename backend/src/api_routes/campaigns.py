from fastapi import APIRouter, HTTPException, status
from ..models.campaign import Campaign
import uuid
import logging

# Create a router to group campaign-related endpoints
router = APIRouter()

# --- Mock Database ---
# In a real application, this would be a connection to a MongoDB collection.
# We use a simple dictionary here for demonstration purposes. It will be shared
# across modules for the duration of the server's runtime.
db = {"campaigns": {}}

# --- API Endpoints ---

@router.post("/campaigns", status_code=status.HTTP_201_CREATED)
async def create_campaign(campaign_data: Campaign):
    """
    Creates a new campaign based on the data sent from the frontend form.

    This endpoint validates the incoming data against the `Campaign` Pydantic model.
    If the data is valid, it assigns a unique ID and stores it in our mock database.

    Args:
        campaign_data (Campaign): The campaign data, automatically parsed and
                                  validated by FastAPI from the request body.

    Returns:
        A confirmation message and the unique ID of the newly created campaign.
    """
    try:
        # Generate a unique ID for the new campaign
        campaign_id = str(uuid.uuid4())
        
        # Store the campaign data in our mock database
        # .dict() converts the Pydantic model back into a dictionary for storage
        db["campaigns"][campaign_id] = campaign_data.dict()
        
        logging.info(f"Campaign created successfully with ID: {campaign_id}")
        return {"message": "Campaign created successfully", "campaign_id": campaign_id}
    except Exception as e:
        logging.error(f"Failed to create campaign: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while creating the campaign."
        )

@router.get("/campaigns/{campaign_id}", status_code=status.HTTP_200_OK)
async def get_campaign(campaign_id: str):
    """
    Retrieves the details of a specific campaign from the database.

    This is used by the frontend's DiscoveryPage to fetch the complete campaign
    details after the discovery and analysis process is complete.

    Args:
        campaign_id (str): The unique ID of the campaign to retrieve.

    Returns:
        The campaign data as a dictionary if found.
    
    Raises:
        HTTPException: A 404 error if the campaign ID does not exist.
    """
    if campaign_id in db["campaigns"]:
        logging.info(f"Retrieved campaign with ID: {campaign_id}")
        return db["campaigns"][campaign_id]
    
    logging.warning(f"Attempted to access non-existent campaign with ID: {campaign_id}")
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Campaign not found."
    )