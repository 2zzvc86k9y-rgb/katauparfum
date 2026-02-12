import os
import sys
import django

sys.path.insert(0, r'C:\PROJETS\katauparfum')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'katauparfum.settings')
django.setup()

from shop.models import Category, Product

# Créer les catégories
parfum_cat, _ = Category.objects.get_or_create(
    name='Parfum',
    defaults={'slug': 'parfum'}
)

huile_cat, _ = Category.objects.get_or_create(
    name='Huile de Parfum',
    defaults={'slug': 'huile-de-parfum'}
)

print(f"✓ Catégories créées: {parfum_cat.name}, {huile_cat.name}")

# Produits pour la catégorie Parfum
parfums = [
    {
        'name': 'Essence Précieuse',
        'price': '89.99',
        'description': 'Un parfum raffiné aux notes florales délicates et boisées. Idéal pour les occasions spéciales.',
        'category': parfum_cat,
    },
    {
        'name': 'Luxe Absolu',
        'price': '120.00',
        'description': 'Une fragrance sophistiquée avec des notes d\'ambre et de musc. Pour les vrais connaisseurs.',
        'category': parfum_cat,
    },
    {
        'name': 'Rêve Éternel',
        'price': '75.50',
        'description': 'Un parfum féminin aux notes florales douces et sensuelles. Classique et intemporel.',
        'category': parfum_cat,
    },
]

# Produits pour la catégorie Huile de Parfum
huiles = [
    {
        'name': 'Huile Nuit Étoilée',
        'price': '45.00',
        'description': 'Une huile de parfum concentrée aux notes mystérieuses. Longue tenue garantie.',
        'category': huile_cat,
    },
    {
        'name': 'Huile Rose & Oud',
        'price': '65.00',
        'description': 'Huile premium avec rose de Damas et bois d\'oud. Pour une application ciblée.',
        'category': huile_cat,
    },
    {
        'name': 'Huile Ambre Vanille',
        'price': '55.00',
        'description': 'Une huile chaleureuse et enveloppante. Parfait pour l\'hiver.',
        'category': huile_cat,
    },
]

# Insérer les parfums
for parfum in parfums:
    product, created = Product.objects.get_or_create(
        name=parfum['name'],
        defaults={
            'price': parfum['price'],
            'description': parfum['description'],
            'category': parfum['category'],
            'is_available': True,
        }
    )
    if created:
        print(f"✓ Créé: {product.name} ({product.price}€)")
    else:
        print(f"- Existe déjà: {product.name}")

# Insérer les huiles
for huile in huiles:
    product, created = Product.objects.get_or_create(
        name=huile['name'],
        defaults={
            'price': huile['price'],
            'description': huile['description'],
            'category': huile['category'],
            'is_available': True,
        }
    )
    if created:
        print(f"✓ Créé: {product.name} ({product.price}€)")
    else:
        print(f"- Existe déjà: {product.name}")

print("\n✓ Données de démonstration chargées avec succès!")
print(f"📊 Total produits: {Product.objects.count()}")
