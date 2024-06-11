
      // Import the functions you need from the SDKs you need
      import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.1/firebase-app.js";
      import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.12.1/firebase-analytics.js";
      import { getStorage, ref, uploadString, getDownloadURL  } from 'https://www.gstatic.com/firebasejs/10.12.1/firebase-storage.js';
      // TODO: Add SDKs for Firebase products that you want to use
      // https://firebase.google.com/docs/web/setup#available-libraries

      // Your web app's Firebase configuration
      // For Firebase JS SDK v7.20.0 and later, measurementId is optional
      const firebaseConfig = {
        apiKey: "AIzaSyBaDJtG0iU-mcSt3KegXPtSczV_TJhBWKQ",
        authDomain: "zoomb-os.firebaseapp.com",
        projectId: "zoomb-os",
        storageBucket: "zoomb-os.appspot.com",
        messagingSenderId: "880723983774",
        appId: "1:880723983774:web:7911124c842f0dcdd9aa8f",
        measurementId: "G-X6M9XMR7E9",
      };

      // Initialize Firebase
      const app = initializeApp(firebaseConfig);
      console.log("aqui chegou no cdigo");
      const analytics = getAnalytics(app);
      const storage = getStorage(app);


                // Initialize SignaturePad instances
            const canvasJard = document.getElementById('canvasAssinatura');
            const signaturePadJard = new SignaturePad(canvasJard);

            const canvasResp = document.getElementById('canvasAssinaturaResp');
            const signaturePadResp = new SignaturePad(canvasResp);

            // Function to clear the canvas
            function limparCanvas(canvas, context) {
                context.clearRect(0, 0, canvas.width, canvas.height);
            }

            // Event listeners for clear buttons
            document.getElementById('btnApagarAssJard').addEventListener('click', function() {
                const contextJard = canvasJard.getContext('2d');
                limparCanvas(canvasJard, contextJard);
            });

            document.getElementById('btnApagarAssResp').addEventListener('click', function() {
                const contextResp = canvasResp.getContext('2d');
                limparCanvas(canvasResp, contextResp);
            });

            //Salvar no fireBase store
            function saveSignatureToFirebase(dataURL, path, callback) {
                const storageRef = ref(storage, `${path}/${Date.now()}.png`);
                uploadString(storageRef, dataURL, 'data_url').then((snapshot) => {
                    getDownloadURL(storageRef).then((downloadURL) => {
                        alert('Assinatura salva com sucesso!');
                        if (callback) callback(downloadURL);
                    });
                }).catch((error) => {
                    console.error('Erro ao fazer o upload da assinatura:', error);
                });
            }

            // Event listeners for save buttons
            document.getElementById('btnSalvarAssJard').addEventListener('click', function() {
                if (signaturePadJard.isEmpty()) {
                    alert('Por favor, desenhe uma assinatura primeiro.');
                    return;
                }
                const dataURL = signaturePadJard.toDataURL('image/png');
                saveSignatureToFirebase(dataURL, 'assinaturas/jardineiro', atualizarCampoAssinaturaJard);
            });

            document.getElementById('btnSalvarAssResp').addEventListener('click', function() {
                if (signaturePadResp.isEmpty()) {
                    alert('Por favor, desenhe uma assinatura primeiro.');
                    return;
                }
                const dataURL = signaturePadResp.toDataURL('image/png');
                saveSignatureToFirebase(dataURL, 'assinaturas/responsavel', atualizarCampoAssinaturaResp);
            });

            // Function to update input fields with signature URL
            function atualizarCampoAssinaturaJard(url) {
                document.getElementById('assinturaJardineiro').value = url;
            }

            function atualizarCampoAssinaturaResp(url) {
                document.getElementById('responsavel').value = url;
            }
            // Função para fechar o modal do Jardineiro após salvar a assinatura
            function fecharModalJardineiro() {
                $('#modalPesquisa').modal('hide'); // Fecha o modal
            }

            // Função para fechar o modal do Responsável após salvar a assinatura
            function fecharModalResponsavel() {
                $('#AssinaturaResp').modal('hide'); // Fecha o modal
            }

    