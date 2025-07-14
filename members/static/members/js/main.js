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
        
    // // Adiciona o evento de clique para CADA um desses botões
    // btnsAbrirModal.forEach(btn => {
    //     btn.addEventListener('click', (event) => {
    //         event.preventDefault(); // Impede a ação padrão do link
    //         const modalId = btn.getAttribute('data-target-modal'); // Pega o valor (ex: '#minha-modal')
    //         const modal = document.querySelector(modalId); // Encontra a modal com esse ID
            
    //         if (modal) {
    //             // ADICIONAMOS a classe 'is-open'
    //             modal.classList.add('is-open'); 
    //         }
    //     });
    // });

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
    try {
        $('#select-membro-advertencia').select2({
            placeholder: "Digite para buscar um membro",
            // Esta linha é MUITO IMPORTANTE para o Select2 funcionar dentro de uma modal
            dropdownParent: $('#nova-advertencia-modal .modal-content')
        });
    } catch(e) {
        console.error("Erro ao inicializar Select2:", e);
    }
    // --- LÓGICA PARA A MODAL DE EDITAR MATERIAL ---
    const editarModal = document.getElementById('editar-material-modal');
    const editarForm = document.getElementById('editar-material-form');
    const btnsEditarMaterial = document.querySelectorAll('.action-edit[data-material-id]');

    btnsEditarMaterial.forEach(btn => {
        btn.addEventListener('click', async (event) => {
            event.preventDefault();
            const materialId = btn.dataset.materialId;

            try {
                // 1. Busca os dados na nossa API
                const response = await fetch(`/members/api/material/${materialId}/`);
                const dados = await response.json();

                // 2. Preenche o formulário da modal com os dados recebidos
                editarForm.querySelector('[name="nome"]').value = dados.nome;
                editarForm.querySelector('[name="tipo"]').value = dados.tipo;
                editarForm.querySelector('[name="finalidade"]').value = dados.finalidade;
                editarForm.querySelector('[name="quantidade_total"]').value = dados.quantidade_total;
                editarForm.querySelector('[name="status"]').value = dados.status;
                editarForm.querySelector('[name="nucleo_responsavel"]').value = dados.nucleo_responsavel_id;

                // 3. Define a URL de ação correta para o formulário
                editarForm.action = `/members/materiais/${materialId}/editar/`;

                // 4. Abre a modal
                editarModal.classList.add('is-open');

            } catch (error) {
                console.error('Erro ao buscar dados do material:', error);
                alert('Não foi possível carregar os dados para edição.');
            }
        });
    });
    const clickableRows = document.querySelectorAll('.clickable-row');
    
    clickableRows.forEach(row => {
        row.addEventListener('click', () => {
            // Pega a URL que colocamos no atributo 'data-href'
            const href = row.dataset.href;
            
            // Se o atributo href existir, navega o navegador para essa página
            if (href) {
                window.location.href = href;
            }
        });
    });
    // Função para pegar o token CSRF dos cookies (essencial para POST com fetch)
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
    const csrftoken = getCookie('csrftoken');


    // Seleciona TODOS os botões que servem para abrir uma modal
        
    btnsAbrirModal.forEach(btn => {
        btn.addEventListener('click', async (event) => { // Tornamos a função assíncrona com 'async'
            event.preventDefault();
            const modalId = btn.getAttribute('data-target-modal');
            const modal = document.querySelector(modalId);

            // --- NOVA LÓGICA DE MARCAR COMO LIDO ---
            // Verificamos se o botão clicado é para ver uma mensagem
            if (btn.classList.contains('action-view-message')) {
                const mensagemId = btn.dataset.messageId;
                try {
                    // Faz a chamada POST para nossa API
                    await fetch(`/members/api/mensagens/${mensagemId}/marcar-lida/`, {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken': csrftoken, // Token de segurança
                            'Content-Type': 'application/json'
                        }
                    });
                    // Atualiza a tag na página sem precisar recarregar
                    const statusTag = btn.closest('tr').querySelector('.tag');
                    if (statusTag) {
                        statusTag.classList.remove('tag-blue');
                        statusTag.classList.add('tag-gray');
                        statusTag.textContent = 'Lida';
                    }
                } catch (error) {
                    console.error("Erro ao marcar mensagem como lida:", error);
                }
            }
            // --- FIM DA NOVA LÓGICA ---
            
            if (modal) {
                modal.classList.add('is-open');
            }
        });
    });

});