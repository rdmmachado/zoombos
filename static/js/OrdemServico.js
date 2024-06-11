

//Abilitar e desabilitar campo Serviço
    function toggleOutrosDescricao() {
        var outrosCheckbox = document.getElementById('outrosServ');
        var outrosDescricao = document.getElementById('outrosServdescricao');

        // Se a opção "Outros" estiver marcada, mostra o campo de descrição, caso contrário, oculta
        if (outrosCheckbox.checked) {
            outrosDescricao.style.display = 'block';
        } else {
            outrosDescricao.style.display = 'none';
        }
    }

    // Adiciona um listener para o evento 'change' no checkbox de outros
    document.getElementById('outrosServ').addEventListener('change', toggleOutrosDescricao);

    ///////////////////////////////
    // Aqui onde eu populo os meus clientes
    function checkOtherOption() {
        var select = document.getElementById("cliente_id");
        var outroInput = document.getElementById("NomeCliente");

        if (select.value === "outroCliente") { // Se a opção "Outros " for selecionada
            outroInput.style.display = "block"; // Mostrar o campo de texto
        } else {
            outroInput.style.display = "none"; // Esconder o campo de texto
            outroInput.value = " "
        }
    }


    // Aqui e onde vai conter a funçãoAssinatura
    var canvasJardim = document.getElementById('canvasAssinatura');
    var canvasRespo = document.getElementById('canvasAssinaturaResp');
    var spadJardim = new SignaturePad(canvasJardim);
    var SpadRespo = new SignaturePad(canvasRespo);

    //Assianatura Jardineiro
    var campoAssinatura = document.getElementById('assinturaJardineiro');
    campoAssinatura.addEventListener('click', function() {
        canvasJardim.style.display = 'block';
    });

    //Assinatura Responsavel
    var campoAssinaturaResp = document.getElementById('assinturaResponsavel');
    campoAssinaturaResp.addEventListener('click', function() {
        SpadRespo.style.display = 'block';
    });


// <!-- Função para validações -->


    function validarFormularioSer() {

        // Verificar se pelo menos um tipo de serviço foi selecionado
        var limpeza = document.getElementById("limpeza").checked;
        var podaGrama = document.getElementById("poda-grama").checked;
        var podaPlantas = document.getElementById("poda-plantas").checked;
        var outros = document.getElementById("outrosServ").checked;
        var outrosServdescricao = document.getElementById("outrosServdescricao");

        if (!limpeza && !podaGrama && !podaPlantas && !outros) {
            alert("Selecione pelo menos um tipo de serviço!");
            return false; // Impede o envio do formulário
        }
        if (outros) {
            if (outrosServdescricao != "")
                alert("Descreva o outro Serviço!");
                 return false; // Impede o envio do formulário
        }


        
        //Verificar se outros clientes esta preenchido
        var select = document.getElementById("clientes");
        var outroInput = document.getElementById("outroCliente");

        if (select.value === "outros") { // Se a opção "Outros " for selecionada
            if (outrosClientes =="")
                alert("Selecione pelo menos um tipo de Cliente!");
                return false
          }

        // Outras validações, se necessário
        return true; // Permite o envio do formulário se todas as validações passarem
        }



        
    function VoltarOS() {
        // Limpe os campos do formulário
        document.getElementById('cadOrdemServicoForm').reset();
        window.location.href='ordem_servico'
    }
    
      function validarFormulario() {
        // Verifique se todos os campos obrigatórios estão preenchidos
        var clienteId = document.getElementById('cliente_id').value;
        var dataRealizacao = document.getElementById('dataRealizacao').value;
        var assinaturaJardineiro = document.getElementById('assinturaJardineiro').value;
        var responsavel = document.getElementById('responsavel').value;

        if (!clienteId || !dataRealizacao || !assinaturaJardineiro || !responsavel) {
            // Se algum campo estiver vazio, exiba uma mensagem de erro
            alert('Por favor, preencha todos os campos obrigatórios.');
            return false; // Impede o envio do formulário
        }

        // Se todos os campos obrigatórios estiverem preenchidos, retorne true para permitir o envio do formulário
        return true;
    }