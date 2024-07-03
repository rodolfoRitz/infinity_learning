url = "https://668288524102471fa4c74866.mockapi.io/minhashistorias";

async function carregarHistorias() {
  const res = await fetch(url);
  const historias = await res.json();
  mostrarHistorias(historias);
}

async function editarHistoria() {
  console.log("toaquicaraio");
}

async function excluirHistoria(id) {
  const urlExcluir = `${url}/${id}`;
  const detalhesRequisicao = {
    method: "DELETE",
  };
  console.log(id);
  const reposta = await fetch(urlExcluir, detalhesRequisicao);
  carregarHistorias();
}

async function editarHistoria(id) {
  const inputID = document.querySelector("#id-editar").value;
  const descricaoNova = document.querySelector("#descricao-nova").value;
  const historiaNova = {
    id: id,
    descricao: descricaoNova,
  };
  const detalhesRequisicao = {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(historiaNova),
  };
  const urlEditar = `${url}/${id}`;
  const reposta = await fetch(urlEditar, detalhesRequisicao);
  alert("Sua história sem graça foi editada com sucesso!");
  carregarHistorias();
}

async function criarHistoria() {
  const inputDescricao = document.querySelector("#descricao");
  let descricao = inputDescricao.value;
  try {
    const historia = {
      descricao: descricao,
      likes: 0,
    };
    const detalhesRequisicao = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(historia),
    };
    const res = await fetch(url, detalhesRequisicao);
    alert("Tarefa adicionada com sucesso");
    carregarHistorias();
    inputDescricao.value = "";
  } catch (erro) {
    console.error(erro);
  }
}

async function carregarDadosHistoriaParaEditar(id) {
  const urlHistoriaEspecifica = `${url}/${id}`;
  const reposta = await fetch(urlHistoriaEspecifica);
  const dadosHistoria = await reposta.json();
  const inputID = document.querySelector("#id-editar");
  const inputDescricao = document.querySelector("#descricao-nova");
  inputID.value = dadosHistoria.id;
  inputDescricao.value = dadosHistoria.descricao;
  carregarHistorias();
}

function mostrarHistorias(historias) {
  const listaTasks = document.querySelector("#lista-historias");
  listaTasks.innerHTML = "";
  historias.forEach((historia) => {
    listaTasks.innerHTML += `
        <tr>
            <td>${historia.id}</td>
            <td>${historia.descricao}</td>
            <td>${historia.likes}</td>
            <td>
                <button onclick="carregarDadosHistoriaParaEditar('${historia.id}')">Editar</button>
                <button onclick="excluirHistoria('${historia.id}')">Excluir</button>
            </td>
        </tr>
        `;
  });
}

const formAdd = document.querySelector("#form-adicionar");
formAdd.addEventListener("submit", (evento) => {
  evento.preventDefault();
  criarHistoria();
});

const botaoEditar = document.querySelector(
  '#form-editar button[type="submit"]'
);

formAdd.addEventListener("submit", (evento) => {
  evento.preventDefault();
  criarHistoria();
});

carregarHistorias();
