from django.contrib import admin
from .models import Category, Product, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available', 'created_at']
    list_filter = ['is_available', 'category', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'image_preview']
    
    def image_preview(self, obj):
        """Affiche une prévisualisation de l'image"""
        if obj.image:
            from django.utils.html import format_html
            return format_html(
                '<img src="{}" style="max-width: 250px; max-height: 250px; border-radius: 8px; box-shadow: 0 4px 12px rgba(212, 175, 55, 0.2); border: 2px solid #d4af37;" />',
                obj.image.url
            )
        return "✨ Aucune image"
    
    image_preview.short_description = "👁️ Aperçu"
    
    fieldsets = (
        ('🎁 Informations Produit', {
            'fields': ('name', 'category', 'price', 'is_available')
        }),
        ('📸 Description & Image', {
            'fields': ('description', 'image', 'image_preview')
        }),
        ('📅 Métadonnées', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'price']
    can_delete = False
    fields = ['product', 'quantity', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone', 'delivery_date', 'total_price', 'created_at']
    list_filter = ['delivery_date', 'created_at']
    search_fields = ['full_name', 'phone', 'address']
    readonly_fields = ['created_at', 'get_whatsapp_link']
    inlines = [OrderItemInline]
    
    fieldsets = (
        ('👤 Informations Client', {
            'fields': ('full_name', 'phone', 'address')
        }),
        ('🚚 Détails Livraison', {
            'fields': ('delivery_date', 'total_price')
        }),
        ('💬 Notification WhatsApp', {
            'fields': ('get_whatsapp_link',),
            'classes': ('collapse',)
        }),
        ('⏰ Métadonnées', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def get_whatsapp_link(self, obj):
        """Affiche le lien WhatsApp pour contacter le client"""
        import urllib.parse
        message = obj.get_whatsapp_message()
        whatsapp_url = f"https://wa.me/{obj.phone}?text={urllib.parse.quote(message)}"
        return f'<a href="{whatsapp_url}" target="_blank" style="display: inline-block; background: linear-gradient(135deg, #25D366 0%, #128c7e 100%); color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: 700; box-shadow: 0 4px 12px rgba(37, 211, 102, 0.3);">📱 Contacter sur WhatsApp</a>'
    
    get_whatsapp_link.short_description = '📱 WhatsApp'
    get_whatsapp_link.allow_tags = True
