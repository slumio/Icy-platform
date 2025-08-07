import logging
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from ..config import settings

class EmailService:
    """A service for sending emails via the SendGrid API."""

    @staticmethod
    def send_outreach_email(to_email: str, subject: str, content_html: str) -> bool:
        """
        Sends a single email using SendGrid.

        Args:
            to_email (str): The recipient's email address.
            subject (str): The subject line of the email.
            content_html (str): The HTML body of the email.

        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """
        message = Mail(
            from_email=settings.SENDER_EMAIL,
            to_emails=to_email,
            subject=subject,
            html_content=content_html
        )
        try:
            # In a real application, you would uncomment the next two lines
            # sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            # response = sg.send(message)
            
            # Logging the mock action for demonstration
            logging.info(f"Mock email sent to {to_email} with subject '{subject}'. Status: 202 Accepted")
            # if response.status_code == 202:
            #     return True
            return True # Assume success for mock
        except Exception as e:
            logging.error(f"Failed to send email to {to_email}: {e}")
            return False