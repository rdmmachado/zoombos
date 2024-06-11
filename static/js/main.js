// add hovered class to selected list item
let list = document.querySelectorAll(".navigation li");

function activeLink() {
  list.forEach((item) => {
    item.classList.remove("hovered");
  });
  this.classList.add("hovered");
}

list.forEach((item) => item.addEventListener("mouseover", activeLink));

// Menu Toggle
let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");

toggle.onclick = function () {
  navigation.classList.toggle("active");
  main.classList.toggle("active");
};

function cancelar() {
  // Limpe os campos do formulário
  document.getElementById('meuFormulario').reset();

  // Volte para a tela anterior (página anterior)
  window.history.back();
}


//Ação para fazer consulta no bd cliente

document.getElementById('btnAbrirPesquisaCliente').addEventListener('click', function() {
  window.location.href = '/p_cliente'; // Esta é a rota definida em clientes.py
  $('#modalPesquisaCliente').modal('show');
});

// Função para lidar com a seleção de um cliente
function selectClient(clientName) {
  // Aqui você pode fazer o que quiser com o cliente selecionado
  // Por exemplo, enviar os dados do cliente de volta para a página principal
  // e fechar o modal de pesquisa

  // Aqui, estamos apenas imprimindo o nome do cliente selecionado no console para fins de demonstração
  console.log("Cliente selecionado:", clientName);

  // Fechar o modal de pesquisa
  $('#modalPesquisaCliente').modal('hide');
}
