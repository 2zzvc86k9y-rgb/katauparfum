from django.conf import settings


def currency(request):
    """Expose la devise utilisée dans les templates"""
    return {
        'CURRENCY': getattr(settings, 'DEFAULT_CURRENCY', 'FCFA')
    }


def whatsapp_config(request):
    """Expose le numéro WhatsApp admin dans les templates"""
    return {
        'WHATSAPP_ADMIN_PHONE': getattr(settings, 'WHATSAPP_ADMIN_PHONE', '+33XXXXXXXXX')
    }
