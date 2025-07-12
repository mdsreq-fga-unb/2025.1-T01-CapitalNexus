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
    const btnsAbrirModal = document.querySelectorAll('[data-target-modal]');
        
    // Adiciona o evento de clique para CADA um desses botões
    btnsAbrirModal.forEach(btn => {
        btn.addEventListener('click', (event) => {
            event.preventDefault(); // Impede a ação padrão do link
            const modalId = btn.getAttribute('data-target-modal'); // Pega o valor (ex: '#minha-modal')
            const modal = document.querySelector(modalId); // Encontra a modal com esse ID
            
            if (modal) {
                // ADICIONAMOS a classe 'is-open'
                modal.classList.add('is-open'); 
            }
        });
    });

    // Seleciona TODOS os botões de fechar (seja o 'X' ou o botão 'Cancelar')
    const btnsFecharModal = document.querySelectorAll('.modal .close-button, .modal .btn-cancel');
    btnsFecharModal.forEach(btn => {
        btn.addEventListener('click', () => {
            // Encontra a modal "mãe" do botão que foi clicado
            const modal = btn.closest('.modal');
            if (modal) {
                //REMOVEMOS a classe 'is-open'
                modal.classList.remove('is-open');
            }
        });
    });

    // Fecha se clicar fora da caixa de conteúdo
    window.addEventListener('click', (event) => {
        // Verifica se o clique foi no fundo escurecido (que tem a classe .modal E a classe .is-open)
        if (event.target.classList.contains('is-open')) {
            event.target.classList.remove('is-open');
        }
    });
    function showTab(tab) {
        document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
        document.getElementById('tab-' + tab).classList.remove('hidden');
    }
});