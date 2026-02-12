"""
Configuration personnalisée pour KATAUPARFUM

Pour modifier les paramètres, éditez ce fichier.
"""

# 📱 WHATSAPP
WHATSAPP_ADMIN_NUMBER = "+33612345678"  # À remplacer par votre numéro WhatsApp

# 🎨 BRANDING
SITE_NAME = "KATAUPARFUM"
SITE_DESCRIPTION = "Boutique en ligne de parfums et huiles de parfum de luxe"
SITE_URL = "http://localhost:8000"  # À adapter en production

# 🚚 LIVRAISON
DELIVERY_OPTIONS = {
    'today': 'Aujourd\'hui',
    'tomorrow': 'Demain'
}

# 📦 PRODUITS
PRODUCTS_PER_PAGE = 12
DEFAULT_CURRENCY = 'FCFA'

# 🎯 SEO
SEO_KEYWORDS = "parfum, huile, luxe, boutique en ligne"
SEO_AUTHOR = "KATAUPARFUM"

# 💡 DEBUG (à mettre à False en production!)
DEBUG_TOOLTIPS = True

# 📧 EMAIL (optionnel)
EMAIL_FROM = "katauparfum.com"
EMAIL_ADMIN = "admin@katauparfum.com"
