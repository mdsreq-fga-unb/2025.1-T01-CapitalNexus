document.addEventListener('DOMContentLoaded', function() {
    const sidebarToggle = document.getElementById('mobile-sidebar-toggle');
    const sidebar = document.querySelector('.sidebar');

    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.toggle('is-open');
        });

        // Opcional: fechar a sidebar se clicar fora dela
        document.addEventListener('click', function(event) {
            // Verifica se o clique foi fora da sidebar E fora do botão de toggle
            const isClickInsideSidebar = sidebar.contains(event.target);
            const isClickOnToggle = sidebarToggle.contains(event.target);

            if (!isClickInsideSidebar && !isClickOnToggle && sidebar.classList.contains('is-open')) {
                sidebar.classList.remove('is-open');
            }
        });
    }
    // --- LÓGICA PARA A MODAL DE MARCAR REUNIÃO ---
    const novaReuniaoModal = document.getElementById('nova-reuniao-modal');
    const btnAbrirModalReuniao = document.getElementById('btn-abrir-modal-reuniao');

    if (novaReuniaoModal && btnAbrirModalReuniao) {
        const btnFechar = novaReuniaoModal.querySelector('.close-button');
        const btnCancelar = novaReuniaoModal.querySelector('.btn-cancel');

        // Quando o usuário clica para ABRIR
        btnAbrirModalReuniao.addEventListener('click', function() {
            novaReuniaoModal.classList.add('is-open'); // MUDANÇA: Adiciona a classe
        });

        // Função para fechar a modal
        const fecharModal = function() {
            novaReuniaoModal.classList.remove('is-open'); // MUDANÇA: Remove a classe
        }

        // Quando o usuário clica no 'X' ou em 'Cancelar' para FECHAR
        if (btnFechar) btnFechar.addEventListener('click', fecharModal);
        if (btnCancelar) btnCancelar.addEventListener('click', fecharModal);

        // Quando o usuário clica fora da caixa de conteúdo
        window.addEventListener('click', function(event) {
            if (event.target == novaReuniaoModal) {
                fecharModal();
            }
        });
    }
});