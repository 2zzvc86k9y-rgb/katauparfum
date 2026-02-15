/**
 * Gestion du panier et des interactions client (AJAX)
 * Empêche le rechargement de la page lors de l'ajout au panier
 */

document.addEventListener('DOMContentLoaded', function() {
    
    // 1. GESTION AJOUT AU PANIER (SANS RECHARGEMENT)
    // Recherche tous les boutons qui servent à ajouter au panier
    // Assurez-vous que vos boutons HTML ont la classe 'add-to-cart-btn' et l'attribut 'data-product-id'
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn, .btn-add-cart, button[type="submit"].add-cart');

    addToCartButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault(); // 🛑 C'est ici qu'on empêche le rechargement !

            // Récupération de l'ID produit (via data-attribute ou value)
            const productId = this.getAttribute('data-product-id') || this.value;
            
            if (!productId) {
                console.error("Aucun ID produit trouvé sur le bouton");
                // Si pas d'ID, on laisse le comportement par défaut (rechargement)
                return; 
            }

            // URL d'ajout (Standard Django)
            const url = '/add-to-cart/'; 

            // Appel AJAX
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    product_id: productId,
                    quantity: 1
                })
            })
            .then(response => {
                if (response.ok) return response.json();
                throw new Error('Erreur réseau');
            })
            .then(data => {
                if (data.success) {
                    // 1. Mettre à jour le badge du panier
                    updateCartBadge(data.cart_count);
                    
                    // 2. Feedback visuel : Change le texte du bouton temporairement
                    const originalText = btn.innerHTML;
                    btn.innerHTML = '✅ Ajouté';
                    
                    setTimeout(() => {
                        btn.innerHTML = originalText;
                    }, 2000);
                    
                } else {
                    alert("Erreur : " + data.message);
                }
            })
            .catch(err => console.error(err));
        });
    });
});

// Fonction pour mettre à jour tous les compteurs de panier sur la page
function updateCartBadge(count) {
    const badges = document.querySelectorAll('.cart-count, #cart-badge');
    badges.forEach(badge => {
        badge.textContent = count;
        // Affiche le badge seulement s'il y a des articles
        if (badge.style) badge.style.display = count > 0 ? 'inline-flex' : 'none';
    });
}

// Récupération du CSRF Token (Nécessaire pour Django)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}