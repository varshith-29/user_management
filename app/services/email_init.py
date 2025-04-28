from functools import lru_cache
from app.services.email_service import EmailService
from app.utils.template_manager import TemplateManager

@lru_cache()
def get_email_service() -> EmailService:
    template_manager = TemplateManager()
    return EmailService(template_manager=template_manager)
