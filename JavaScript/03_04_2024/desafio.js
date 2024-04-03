// https://messy-button-d76.notion.site/2f5689fab90642e3974eda41afa0358e?v=4ee20c583fab4ef5ad73d26980d18ad1
// Este endereço CONTEM TODAS AS AULAS DE JAVASCRIPT.

// Uma empresa de pesquisas precisa tabular os
// resultados da seguinte enquete feita a um grande

// quantidade de organizações:

// "Qual o melhor Sistema Operacional para uso em

// servidores?" As possíveis respostas são:

// 1- Windows Server

// 2- Unix
// 3- Linux
// 4- Netware
// 5- Mac OS
// 6- Outro
// -------------------------------------------------
// Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado
// o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada
// uma das opções devem ser armazenados num vetor. 

// Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e
// informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

// Sistema Operacional Votos %
// ------------------- ----- ---
// Windows Server 1500 17%
// Unix 3500 40%
// Linux 3000 34%
// Netware 500 5%
// Mac OS 150 2%
// Outro 150 2%
// ------------------- ----- Total : 8800

let vetor = []
let impar = []
let par = []

for (let i = 1; i < 21; i++) {

    let num = i
    vetor.unshift(num)

    if (num % 2 === 0) {
        par.unshift(num)
    }
    else {
        impar.unshift(num)
    }
} 
console.log(`Valores digitados: ${vetor}`)
console.log(`Valores ímpares: ${impar}`)
console.log(`Valores pares: ${par}`)
