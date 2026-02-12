from django.db import models
from django.utils.text import slugify
from PIL import Image


class Category(models.Model):
    """Catégorie de produits (Parfum / Huile de parfum)"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    """Produits (parfums et huiles de parfum)"""
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['is_available', 'category']),
        ]

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    def save(self, *args, **kwargs):
        """Redimensionne et compresse l'image automatiquement à la sauvegarde"""
        super().save(*args, **kwargs)

        if self.image:
            try:
                img = Image.open(self.image.path)
                # Si l'image est plus grande que 1200px, on la réduit (Qualité Luxe HD)
                if img.height > 1200 or img.width > 1200:
                    output_size = (1200, 1200)
                    img.thumbnail(output_size)
                    # Sauvegarde optimisée (qualité 85%)
                    img.save(self.image.path, quality=85, optimize=True)
            except Exception:
                pass  # On ignore les erreurs si le fichier n'est pas accessible


class Order(models.Model):
    """Commande du client"""
    DELIVERY_CHOICES = [
        ('today', 'Aujourd\'hui'),
        ('tomorrow', 'Demain'),
    ]

    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)  # Numéro WhatsApp
    address = models.TextField()
    delivery_date = models.CharField(max_length=10, choices=DELIVERY_CHOICES)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Commande #{self.id} - {self.full_name}"

    def get_whatsapp_message(self):
        """Génère le message WhatsApp pour la commande"""
        items_text = "\n".join([
            f"• {item.product.name} × {item.quantity} - {item.price} FCFA"
            for item in self.orderitem_set.all()
        ])
        
        delivery_text = "Aujourd'hui" if self.delivery_date == 'today' else "Demain"
        
        message = f"""*Nouvelle Commande KATAUPARFUM*

*Client:* {self.full_name}
*Téléphone:* {self.phone}
*Adresse:* {self.address}

*Produits:*
{items_text}

*Total:* {self.total_price} FCFA
*Livraison:* {delivery_text}

Commande ID: #{self.id}"""
        
        return message


class OrderItem(models.Model):
    """Ligne d'une commande"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('order', 'product')

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"
