// node .\scripts.js - Comando "do Terminal", que executa e mostra o resultado no Terminal.

let esportes = ['volei', 'futebol', 'polo']

esportes.splice(2, 0, 'natacao', 'xadrez')
tamanho_array = esportes.length

console.log('Tamanho:', tamanho_array, '----', esportes)

let array = [6, 7, 8]

mostrar_array = array.sort() // Função que ordena os elementos de um Array.
mostrar_posicao = array.indexOf(7) // Função que mostra a POSIÇÃO do elemento no Array.

console.log(mostrar_array)
console.log(mostrar_posicao)

for (let letra of array) {
    if (letra === 'a') {
        console.log('A letra atual é a letra A.')
    }
    else {
        console.log('Não é a letra A.')
    }
} 