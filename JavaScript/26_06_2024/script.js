const url = "https://667c872b3c30891b865cebd6.mockapi.io/historia/historia";
          // https://mockapi.io/projects/667c872b3c30891b865cebd7#
          

async function carrregarHistoria() {
  const resposta = await fetch(url);
  const dados = await resposta.json();
//   colocarNoHtml(dados);
  console.log(dados);
}
carrregarHistoria();

async function criarHistoria() {
    const inputDescricao = document.querySelector('#descricao')
    // const descricaoInformada = document.querySelector("#descricao");
    let descricaoDigitada = inputDescricao.value
    const historiaCriada = {
        descricao: descricaoDigitada,
        likes: 0,
    }
  const resposta = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(historiaCriada),
  })
  alert('Sua história foi criada!')
}

function colocarNoHtml(historias) {
  const tabelaHistoria = document.querySelector("#lista-historias");
  tabelaHistoria.innerHTML = "";

  historias.forEach((historia) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `

            <td>${historia.id}</td>
            <td>${historia.descricao}</td>
            <td>${historia.likes}</td>
        `;
    tabelaHistoria.appendChild(tr);
  });
}

const formularioCadastrarHistoria = document.querySelector("#form-adicionar");
formularioCadastrarHistoria.addEventListener("submit", (evento) => {
  evento.preventDefault();
  criarHistoria();
});
