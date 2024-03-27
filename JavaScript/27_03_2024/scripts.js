// let contador = 7

// do {
//     if (contador === 4){
//         continue
//     }
//     console.log(`Contador ${contador} vez(es)`) 
//     contador++
// } while (contador < 0)

// let nota = 0
// let contador = 0
// let media = 0
// let total_notas = 0

// while (nota != 40){
//     nota = Number(prompt(`Digite sua nota: `))
//     total_notas = total_notas + nota
//     contador++
// }
// media = total_notas / contador
// console.log(`A média das notas é: `+media)

let saldo_conta_corrente = 1000
let fatura_cartao_credito = 0
let p_todas = 0

while (p_todas != 4){
    p_todas = Number(prompt('Qual operação deseja realizar? \nPara saque digite 1. \nPara saldo atual digite 2. \nPara realizar um NOVO depósito digite 3. \nPara SAIR digite 4'))
    console.log(1 == '1')
    if (p_todas === 1){
        valor_saque = prompt(`Digite o valor do saque: `)
        if ((valor_saque > 0) && (valor_saque <= saldo_conta_corrente)){ 
            saldo_conta_corrente = saldo_conta_corrente - valor_saque
            console.log(`Sucesso! Seu saldo atual é: ${saldo_conta_corrente}`)
        }
        else {
            console.log('Saque NÃO autorizado. Digite um valor válido.')
            continue
        }
        continue
    }
    else if (p_todas === 2){
        prompt(`Seu saldo atual é: ${saldo_conta_corrente}`)
        continue
    }
    else if (p_todas === 3){
        let valor_deposito = Number(prompt(`Digite o valor a ser depositado: `))
        saldo_conta_corrente = saldo_conta_corrente + valor_deposito
        console.log(`Seu saldo atual é: ${saldo_conta_corrente}`)
        continue
    }
    else if (p_todas === 4){
        console.log('Você foi DESCONECTADO com sucesso.')
        break
    }
}
