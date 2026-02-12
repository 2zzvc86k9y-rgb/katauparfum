# 💎 KATAUPARFUM - Boutique E-commerce de Luxe

Bienvenue sur **KATAUPARFUM**, une boutique en ligne élégante et mobile-first pour la vente de parfums et huiles de parfum de luxe.

## 🚀 Démarrage Rapide

### Prérequis
- Python 3.10+
- MySQL Server
- Un numéro WhatsApp pour les notifications

### Installation

1. **Activer l'environnement virtuel** (sur Windows PowerShell):
```powershell
.\env\Scripts\Activate.ps1
```

2. **Appliquer les migrations** (déjà fait):
```bash
python manage.py migrate
```

3. **Charger les données de démonstration** (déjà fait):
```bash
python load_demo_data.py
```

4. **Créer un superutilisateur** (déjà fait):
- Username: `admin`
- Password: `admin123`
- Email: `admin@katauparfum.com`

5. **Lancer le serveur de développement**:
```bash
python manage.py runserver
```

6. **Accéder à l'application**:
- 🏪 Boutique: http://localhost:8000/
- 🔧 Admin: http://localhost:8000/admin/

---

## 📁 Structure du Projet

```
katauparfum/
├── katauparfum/           # Configuration Django
│   ├── settings.py        # Paramètres du projet
│   ├── urls.py           # URLs principales
│   └── wsgi.py           # WSGI config
├── shop/                  # Application Django
│   ├── models.py         # Modèles de données
│   ├── views.py          # Vues (logique métier)
│   ├── urls.py           # URLs de shop
│   ├── admin.py          # Admin Django
│   └── migrations/       # Migrations DB
├── templates/            # Templates HTML
│   ├── base.html        # Template de base
│   ├── home.html        # Accueil
│   ├── products.html    # Listing produits
│   ├── cart.html        # Panier
│   ├── checkout.html    # Commande
│   └── order_confirmation.html  # Confirmation
├── static/              # Fichiers statiques
│   ├── css/            # Styles Tailwind
│   └── js/             # JavaScripts
├── media/              # Uploads (images produits)
├── manage.py           # CLI Django
├── load_demo_data.py   # Script de démo
└── set_admin_password.py  # Script admin
```

---

## 🧴 Modèles de Données

### Category
- `name`: Nom de la catégorie (Parfum / Huile de parfum)
- `slug`: URL-friendly identifier

### Product
- `name`: Nom du produit
- `category`: Catégorie (FK)
- `price`: Prix en euros
- `image`: Image du produit
- `description`: Description détaillée
- `is_available`: Disponibilité

### Order
- `full_name`: Nom complet du client
- `phone`: Numéro WhatsApp
- `address`: Adresse de livraison
- `delivery_date`: Aujourd'hui ou demain
- `total_price`: Montant total
- `created_at`: Date de création

### OrderItem
- `order`: FK vers Order
- `product`: FK vers Product
- `quantity`: Quantité commandée
- `price`: Prix unitaire à la commande

---

## 🛒 Fonctionnalités

### ✅ Pour les Clients
- ✓ Voir tous les produits avec filtrage par catégorie
- ✓ Ajouter/retirer des produits du panier
- ✓ Modifier les quantités en temps réel
- ✓ Panier géré via sessions Django (pas d'inscription)
- ✓ Formulaire de commande simple et intuitif
- ✓ Choix de livraison: Aujourd'hui ou Demain
- ✓ Lien WhatsApp dynamique généré automatiquement
- ✓ Page de confirmation avec récapitulatif

### ✅ Pour l'Admin
- ✓ Gestion complète des produits
- ✓ Gestion des catégories
- ✓ Historique des commandes
- ✓ Lien WhatsApp direct pour contacter les clients
- ✓ Détails complets de chaque commande

---

## 🎨 Design & Responsive

- **Couleurs**: Noir, Or (#d4af37), Blanc
- **Framework CSS**: Tailwind CSS 3
- **Responsive**: Mobile-first design
- **Animations**: Transitions fluides et légères
- **Icons**: Font Awesome 6

---

## 📱 Panier & Session

Le panier est géré entièrement via les **sessions Django**:
```javascript
// Ajouter au panier (JavaScript AJAX)
fetch('/api/add-to-cart/', {
    method: 'POST',
    body: JSON.stringify({product_id: 123, quantity: 1})
})
```

Les données du panier sont stockées dans `request.session['cart']`:
```python
# Format: {product_id: quantity, ...}
{'1': 2, '3': 1}  # 2 × produit 1, 1 × produit 3
```

---

## 🔔 Notification WhatsApp

### Flux de Commande
1. Client remplit le formulaire (nom, WhatsApp, adresse, livraison)
2. Commande enregistrée en base de données
3. Message WhatsApp généré automatiquement avec:
   - Nom du client
   - Téléphone
   - Adresse
   - Liste des produits
   - Total à payer
   - Date de livraison
4. Lien WhatsApp: `https://wa.me/{phone}?text={message}`

### Format du Message
```
*Nouvelle Commande KATAUPARFUM*

*Client:* Jean Dupont
*Téléphone:* +33612345678
*Adresse:* 123 Rue de la Paix, 75000 Paris

*Produits:*
• Essence Précieuse × 2 - 89.99€
• Huile Nuit Étoilée × 1 - 45.00€

*Total:* 224.98€
*Livraison:* Aujourd'hui

Commande ID: #42
```

---

## 🔐 Admin Django

### Accès
- URL: http://localhost:8000/admin/
- Username: `admin`
- Password: `admin123`

### Interfaces Disponibles
1. **Catégories**: Créer/éditer/supprimer
2. **Produits**: Gestion complète avec images
3. **Commandes**: Historique avec lien WhatsApp
4. **Items de Commande**: Affichage en ligne

---

## 🚀 Déploiement

### Avant la Production
1. ✅ Changer `DEBUG = False` dans settings.py
2. ✅ Générer une nouvelle `SECRET_KEY`
3. ✅ Configurer `ALLOWED_HOSTS`
4. ✅ Configurer les credentials MySQL
5. ✅ Ajouter le numéro WhatsApp admin

### Base de Données
```sql
CREATE DATABASE katauparfum_db;
CREATE USER 'katauparfum_user'@'localhost' IDENTIFIED BY 'secure_password';
GRANT ALL PRIVILEGES ON katauparfum_db.* TO 'katauparfum_user'@'localhost';
FLUSH PRIVILEGES;
```

### Variables d'Environnement (recommandé)
```python
# settings.py
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '3306'),
    }
}
```

---

## 📝 Configuration Personnalisée

### Modifier le Numéro WhatsApp
Dans le template `base.html`, ligne ~200:
```html
<a href="https://wa.me/VOTRE_NUMERO" target="_blank">
```

### Modifier le Branding
- Logo: [base.html](templates/base.html) ligne ~30
- Couleurs: [base.html](templates/base.html) `--color-gold: #d4af37`
- Nom: Remplacer "KATAUPARFUM" partout

### Ajouter des Produits
**Via l'Admin**:
1. Aller à http://localhost:8000/admin/shop/product/
2. Cliquer "Ajouter Produit"
3. Remplir les infos et uploader l'image

**Via Django Shell**:
```bash
python manage.py shell
from shop.models import Product, Category
cat = Category.objects.get(name='Parfum')
Product.objects.create(
    name='Mon Parfum',
    price=99.99,
    description='Description',
    category=cat,
    is_available=True
)
```

---

## 🐛 Troubleshooting

### Erreur: "Aucune base de données"
```bash
# Vérifier MySQL est lancé
# Ajuster settings.py avec les bonnes credentials
python manage.py migrate
```

### Erreur: "Images ne s'affichent pas"
- Vérifier que `MEDIA_URL` et `MEDIA_ROOT` sont corrects
- S'assurer que le serveur sert les fichiers statiques
- En dev: Automatique. En prod: Configurer Nginx/Apache

### Panier vide après fermeture
Normal! Le panier est en session (temporaire). Pour le rendre persistant, modifier [views.py](shop/views.py) pour utiliser une base de données.

---

## 📞 Support

Pour ajouter une fonctionnalité:
1. Modifier les modèles dans [shop/models.py](shop/models.py)
2. Créer les migrations: `python manage.py makemigrations`
3. Appliquer: `python manage.py migrate`
4. Ajouter les vues dans [shop/views.py](shop/views.py)
5. Créer les templates dans [templates/](templates/)
6. Enregistrer dans [shop/urls.py](shop/urls.py)

---

## 📄 Licence

Projet privé pour KATAUPARFUM © 2026

---

**Bon shopping! 💎✨**
