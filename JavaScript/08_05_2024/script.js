function recebiClique(){
    console.log('Clicou')
}

const botaoEnviar = document.getElementById('clicar')
botaoEnviar.addEventListener('click', recebiClique)

const inputNome = document.getElementById('nome')

inputNome.addEventListener('input', () => {
    let valorDigitado = inputNome.value
    console.log(`Digitou: ${valorDigitado}`)
})

botao.addEventListener('click', () => {
    let tarefa = document.querySelector('input').value
    const listaTarefas = document.querySelector
})

// Primeira maneira
// botaoEnviar.addEventListener('click', () => {
//     console.log('Clicou')
// }
