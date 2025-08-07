import openai
import logging
from ..config import settings

# In a real application, you would uncomment the next line
# openai.api_key = settings.OPENAI_API_KEY

class AIService:
    """A service for interacting with the OpenAI GPT model."""

    @staticmethod
    def generate_outreach_message(influencer_name: str, brand_name: str, recent_post_topic: str, brand_tone: str) -> str:
        """
        Generates a personalized outreach message using a GPT model.

        This method constructs a detailed prompt based on the input parameters
        to guide the AI in creating a relevant and tone-appropriate message.
        """
        try:
            prompt = (
                f"Write a short, {brand_tone}, and personalized outreach message for a potential brand collaboration.\n"
                f"Your Brand's Name: {brand_name}\n"
                f"Influencer's Name: {influencer_name}\n"
                f"Key Personal Detail: Compliment them on their recent content about '{recent_post_topic}'.\n\n"
                f"Keep the message concise, authentic, and engaging. Start directly with the greeting.\n\n"
                f"Message:"
            )
            logging.info(f"Generating AI message for {influencer_name} with prompt: {prompt}")

            # This is where the actual API call would be made.
            # response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=120)
            # return response.choices[0].text.strip()
            
            # Returning a mock response for demonstration purposes.
            return f"Hi {influencer_name}! Absolutely love your recent post about {recent_post_topic}. We at {brand_name} are big fans of your work and think you'd be a perfect fit for our new campaign. Would you be open to chatting?"
        except Exception as e:
            logging.error(f"Error in AIService while generating message: {e}")
            # Fallback message in case of an AI service failure
            return f"Hi {influencer_name}, we're impressed with your content and would love to discuss a potential collaboration with {brand_name}."

    @staticmethod
    def analyze_content_for_heuristics(posts: list) -> tuple[float, float]:
        """
        Analyzes a list of posts to determine authenticity and sentiment.
        In a real application, this would involve a more complex GPT call
        asking the AI to score the content based on specific criteria.
        """
        logging.info("Performing mock heuristic analysis on posts.")
        if not posts:
            return (70.0, 80.0) # Default scores if no posts are available
        # Mock analysis: returns (authenticity_score, avg_sentiment_score)
        return (85.2, 92.5)