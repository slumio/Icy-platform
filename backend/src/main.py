from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from .api_routes import campaigns, discovery, outreach

# --- Application Setup ---

# Configure logging for better server insights
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create the main FastAPI application instance
app = FastAPI(
    title="ICY Platform API",
    description="The backend engine for the AI-powered influencer outreach platform.",
    version="1.0.0"
)

# --- Middleware Configuration ---

# Configure CORS (Cross-Origin Resource Sharing) to allow requests from your frontend.
# This is a critical security feature that tells the browser it's safe for your
# React app (on localhost:3000) to talk to your backend (on localhost:8000).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # The origin of your React development server
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# --- API Router Mounting ---

# Include the API routers from other modules. This keeps your main file clean
# and organizes your endpoints by functionality.
app.include_router(campaigns.router, prefix="/api", tags=["Campaigns"])
app.include_router(discovery.router, prefix="/api", tags=["Discovery & Scoring"])
app.include_router(outreach.router, prefix="/api", tags=["Outreach"])

# --- Root Endpoint ---

@app.get("/", tags=["Root"])
async def read_root():
    """
    A simple root endpoint to confirm that the server is running.
    """
    return {"message": "Welcome to the ICY Platform API"}

# This is a simple hack to share the in-memory "database" between modules
# for this demonstration. In a real app with a proper database connection,
# this would not be necessary.
from .api_routes.discovery import db as discovery_db
from .api_routes.campaigns import db as campaigns_db
campaigns_db.update(discovery_db)