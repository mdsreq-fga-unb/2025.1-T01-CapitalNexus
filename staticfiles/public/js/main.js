document.addEventListener('DOMContentLoaded', function() {

    // =========================================================
    // LÓGICA DO MENU MOBILE
    // =========================================================
    const mobileMenuIcon = document.querySelector('.menu-mobile-icon');
    const mobileMenu = document.querySelector('.menu-mobile');

    if (mobileMenuIcon && mobileMenu) {
        mobileMenuIcon.addEventListener('click', function() {
            mobileMenu.classList.toggle('active');
        });
    }

    // =========================================================
    // LÓGICA DA JANELA MODAL DE TERMOS
    // =========================================================
    const modal = document.getElementById('terms-modal');
    const openModalLink = document.getElementById('open-terms-modal');
    const closeModalButton = document.querySelector('.close-button');

    if (modal && openModalLink && closeModalButton) {
        
        // Quando o usuário clica no link "termos de uso"
        openModalLink.addEventListener('click', function(event) {
            event.preventDefault(); // Impede o link de pular para o topo da página
            modal.style.display = 'block';
        });

        // Quando o usuário clica no 'X' para fechar
        closeModalButton.addEventListener('click', function() {
            modal.style.display = 'none';
        });

        // Quando o usuário clica fora da caixa de conteúdo, fecha a modal também
        window.addEventListener('click', function(event) {
            if (event.target == modal) {
                modal.style.display = 'none';
            }
        });
    }

});