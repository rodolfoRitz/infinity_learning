// function saudar() {
//     let nome = document.querySelectorAll('#nome')
//     let nomeDigitado = nome[0].value
//     console.log(`Olá ${nomeDigitado}`)
// }
// let titulo = document.querySelector('title')
// titulo.innerText = 'Aula 8'


// Pegando valores de um input:
// function colocarTexto(){
//     let caixaTexto = document.querySelector("#meuTexto")
//     let textoDentro = caixaTexto.value
//     console.log(textoDentro)
// }


// Adicionando elementos no HTML:
// let novo_elemento =  document.createElement("p")
// novo_elemento.textContent = "OLá mundo!"
// let div_novo_texto = document.querySelector("#div_mae")
// div_novo_texto.appendChild(novo_elemento)


// Trocando valores de um p:
// let p_troca =  document.getElementById("alterado")
// p_troca.textContent = 'Olá'


// DESAFIO PRÁTICO (mostrar para o Prata)
let novo_elemento = document.createElement("li")
let caixaTexto = document.querySelector("#meuTexto")

function adicionarTarefa() {
    var novaTarefa = document.getElementById("inputTarefa").value;
    
    if (novaTarefa !== '') {
        var lista = document.getElementById("listaTarefas");
        var novaTarefaItem = document.createElement("li");
        // Adicionar a tarefa ao item de lista
        novaTarefaItem.innerText = novaTarefa;
        // Adicionar o botão de exclusão à tarefa
        var botaoExcluir = document.createElement("button");
        botaoExcluir.innerText = "Excluir";
        botaoExcluir.onclick = function() {
            this.parentNode.remove();
        };
        // Adicionar a tarefa e o botão de exclusão à lista
        novaTarefaItem.appendChild(botaoExcluir);
        lista.appendChild(novaTarefaItem);
        // Limpar o campo de entrada
        document.getElementById("inputTarefa").value = '';
    } else {
        alert("Por favor, insira uma tarefa.");
    }
}

function marcarConcluida(event) {
    var tarefa = event.target;
    tarefa.classList.toggle("concluida");
}

function removerTarefa(event) {
    var botaoExcluir = event.target;
    var tarefa = botaoExcluir.parentNode;
    tarefa.remove();
}
