# ICY Platform API Reference

Welcome to the official API documentation for the ICY Influencer Platform. This guide provides all the information you need to interact with the backend services.

**Base URL**: All API routes are prefixed with `/api`. For local development, the full base URL is `http://localhost:8000/api`.

---

## Campaigns

Endpoints for creating and managing marketing campaigns.

### `POST /campaigns`

Creates a new campaign. This is the first step in any workflow. The backend will validate the request body against the `Campaign` model.

**Request Body:**

```json
{
  "user_id": "user123",
  "campaign_name": "Summer Skincare Launch",
  "brand_profile": {
    "product_details": "Organic, vegan skincare products for sensitive skin.",
    "target_audience": {
      "age": [25, 35],
      "gender": "Female",
      "interests": ["sustainability", "clean beauty"]
    },
    "brand_tone": "friendly",
    "budget": "micro",
    "niche": ["beauty", "sustainability"]
  }
}
```

**Success Response (201 Created):**

```json
{
  "message": "Campaign created successfully",
  "campaign_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef"
}
```

**Error Response (422 Unprocessable Entity):**
This occurs if the request body is missing required fields or has incorrect data types.

---

### `GET /campaigns/{campaign_id}`

Retrieves the full details for a specific campaign, including any discovered influencers.

**URL Parameters:**
- `campaign_id` (string, required): The unique ID of the campaign.

**Success Response (200 OK):**
Returns the complete `Campaign` object.

```json
{
  "user_id": "user123",
  "campaign_name": "Summer Skincare Launch",
  "brand_profile": { ... },
  "discovered_influencers": [
    {
      "handle": "Emma_GreenBeauty",
      "platform": "Instagram",
      "followers": 25000,
      "engagement_rate": 4.5,
      "niche": ["sustainability", "beauty"],
      "scores": {
        "brand_fit_score": 92.5,
        "authenticity_score": 85.2,
        "audience_match_score": 85.0,
        "engagement_quality": "High"
      }
    }
  ],
  "status": "discovery_complete"
}
```

**Error Response (404 Not Found):**
Occurs if the `campaign_id` does not exist.

---

## Discovery & Scoring

Endpoint for running the AI-powered analysis.

### `POST /campaigns/{campaign_id}/discover`

Triggers the backend process to find, analyze, and score influencers based on the campaign's brand profile. This is a long-running task. The response is sent after the process is complete.

**URL Parameters:**
- `campaign_id` (string, required): The unique ID of the campaign to run discovery for.

**Success Response (200 OK):**

```json
{
  "message": "Discovery complete",
  "influencer_count": 3
}
```

---

## Outreach

Endpoint for generating personalized messages.

### `POST /generate-message`

Uses the AI service to craft a personalized outreach message for a specific influencer.

**Request Body:**

```json
{
  "influencer_name": "Emma",
  "brand_name": "EcoGlow Skincare",
  "recent_post_topic": "clean beauty ingredients",
  "brand_tone": "friendly"
}
```

**Success Response (200 OK):**

```json
{
  "message": "Hi Emma! Absolutely love your recent post about clean beauty ingredients. We at EcoGlow Skincare are big fans of your work and think you'd be a perfect fit for our new campaign. Would you be open to chatting?"
}