const botao = document.querySelector("button");
const cep = document.querySelector("#cep");

const logradouro = document.querySelector("input#logradouro");
console.log(logradouro)
const bairro = document.querySelector("input#bairro");
const localidade = document.querySelector("input#localidade");
const uf = document.querySelector("input#uf");

botao.addEventListener("click", (event) => {
  event.preventDefault()
  const cepDigitado = cep.value;
  const url = `https://viacep.com.br/ws/${cepDigitado}/json/`;
  // console.log("oi");
  // debugger;
  fetch(url)
    .then((resposta) => {
      return resposta.json();
    })
    .then((dados) => {
      console.log(dados);
      logradouro.value = dados.logradouro;
      bairro.value = dados.bairro;
      localidade.value = dados.localidade;
      uf.value = dados.uf;
    });
});

// {
//     "cep": "30190-060",
//     "logradouro": "Rua dos Tupis",   --
//     "complemento": "até 240/241",
//     "bairro": "Centro",              --
//     "localidade": "Belo Horizonte",  --
//     "uf": "MG",                      --
//     "ibge": "3106200",
//     "gia": "",
//     "ddd": "31",
//     "siafi": "4123"
// }
