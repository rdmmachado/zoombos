

 const canvasJard = document.getElementById('canvasAssinatura');
 const signaturePadJard = new SignaturePad(canvasJard);

 const canvasResp = document.getElementById('canvasAssinaturaResp');
 const signaturePadResp = new SignaturePad(canvasResp);
 const storage = getStorage();

  // Função para limpar o canvas
    function limparCanvas(canvas, context) {
         context.clearRect(0, 0, canvas.width, canvas.height);
    }

     // Adicionar evento de clique nos botões de apagar
    document.getElementById('btnApagarAssJard').addEventListener('click', function () {
      var canvasJard = document.getElementById('canvasAssinatura');
         var contextJard = canvasJard.getContext('2d');
         limparCanvas(canvasJard, contextJard); // Limpar o canvas do responsável
     });

    document.getElementById('btnApagarAssResp').addEventListener('click', function () {
        var canvasResp = document.getElementById('canvasAssinaturaResp');
         var contextResp = canvasResp.getContext('2d');
        limparCanvas(canvasResp, contextResp); // Limpar o canvas do responsável
    });
  // ------------------------------

   // Função para fechar o modal do Jardineiro após salvar a assinatura
 function fecharModalJardineiro() {
    $('#modalPesquisa').modal('hide'); // Fecha o modal
}

// Função para fechar o modal do Responsável após salvar a assinatura
function fecharModalResponsavel() {
    $('#AssinaturaResp').modal('hide'); // Fecha o modal
}

    // const storage = firebase.storage();
    // const storageRef = storage.ref();
     

     document.getElementById('btnSalvarAssJard').addEventListener('click', function() {
        if (signaturePadJard.isEmpty()) {
            alert('Por favor, desenhe uma assinatura primeiro.');
            return;
        }
        
        console.log('Aqui e o entra pra salvar');
        const dataURL = signaturePadJard.toDataURL('image/png');
        saveSignatureToFirebase(dataURL, 'assinaturas/jardineiro');//, atualizarCampoAssinaturaJard);
    });
    
    document.getElementById('btnSalvarAssResp').addEventListener('click', function(){
        if (signaturePadResp.isEmpty()) {
            alert('Por favor, desenhe uma assinatura primeiro.');
            return;
        }
        const dataURL = signaturePadResp.toDataURL('image/png');
        saveSignatureToFirebase(dataURL, 'assinaturas/responsavel'); // , atualizarCampoAssinaturaResp);
    });


        function saveSignatureToFirebase(dataURL, path) {
            console.log('Aqui dentro da função');
            const storageRef = ref(storage, `${path}/${Date.now()}.png`);
            console.log('Aqui no Storage para acessar', storageRef);

            uploadString(storageRef, dataURL, 'data_url').then((snapshot) => {
                console.log('apos o upload');
                snapshot.ref.getDownloadURL().then((downloadURL) => {
                    alert('Assinatura salva com sucesso!');
                    // Aqui você pode chamar a função de fechar o modal, se necessário
                    // fecharModal();
                });
            }).catch((error) => {
                console.error('Erro ao fazer o upload da assinatura:', error);
            });
        }

    // function saveSignatureToFirebase(dataURL, path, updateFieldCallback) {
    //     const storageRef = firebase.storage().ref();
    //     const fileName = `${path}/${Date.now()}.png`;
    //     const imageRef = storageRef.child(fileName);
    //     console.log("Ate aqui")
    //     imageRef.putString(dataURL, 'data_url').then((snapshot) => {
    //         snapshot.ref.getDownloadURL().then((downloadURL) => {
    //             updateFieldCallback(downloadURL);
    //             alert('Assinatura salva com sucesso!');
    //             fecharModal();
    //         });
    //     }).catch((error) => {
    //         console.error('Erro ao fazer o upload da assinatura:', error);
    //     });
    // }

     
// // Função para atualizar o valor dos campos de assinatura com o URL
//  function atualizarCampoAssinaturaJard(url) {
//     document.getElementById('assinturaJardineiro').value = url;
//  }

//  function atualizarCampoAssinaturaResp(url) {
//      document.getElementById('responsavel').value = url;
//  }




