/**
 * Script de réparation pour l'interface Admin Jazzmin
 * Force les liens de profil et initialise les composants UI
 */
document.addEventListener("DOMContentLoaded", function() {
    // 1. Réparer le menu profil (le petit bonhomme)
    // On remplace le href vide par '#' pour éviter le rechargement ou l'inaction
    const userProfileLinks = document.querySelectorAll('.user-menu .dropdown-toggle, .nav-item.dropdown .nav-link');
    
    userProfileLinks.forEach(function(link) {
        link.setAttribute('href', '#');
        
        // Force l'ouverture au clic si Bootstrap ne le fait pas
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const parent = this.parentElement;
            if (parent) {
                parent.classList.toggle('show');
                const menu = parent.querySelector('.dropdown-menu');
                if (menu) menu.classList.toggle('show');
            }
        });
    });

    // 2. S'assurer que les "Collaps" (Fieldsets des produits) sont cliquables
    const collapseToggles = document.querySelectorAll('a[data-toggle="collapse"]');
    collapseToggles.forEach(function(toggle) {
        // FIX: On ne touche PAS au href ici, car il contient l'ID de la section à ouvrir !
        
        toggle.addEventListener('click', function(e) {
            e.preventDefault(); // Empêche le saut en haut de page
            
            // Fallback manuel : Si Bootstrap ne gère pas le clic, on le fait nous-mêmes
            const targetId = this.getAttribute('href');
            if (targetId && targetId.startsWith('#')) {
                const target = document.querySelector(targetId);
                if (target) {
                    // On bascule manuellement la classe 'show' pour afficher/masquer
                    // Cela garantit le fonctionnement même si le JS de Jazzmin a un conflit
                    const isVisible = target.classList.contains('show');
                    if (isVisible) {
                        target.classList.remove('show');
                        this.classList.add('collapsed');
                    } else {
                        target.classList.add('show');
                        this.classList.remove('collapsed');
                    }
                }
            }
        });
    });
});