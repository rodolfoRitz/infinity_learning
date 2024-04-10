let contador = 0;
let palavra = 'abacate';

function contarVogais(palavra) {
    for (let i = 0; i < palavra.length; i++) {
        let letra = palavra[i].toLowerCase(); // convert to lowercase for case-insensitivity
        if (letra === 'a' || letra === 'e' || letra === 'i' || letra === 'o' || letra === 'u') {
            contador = contador + 1;
        }
    }
}

contarVogais(palavra);
console.log(contador);

// const readlineSync = require('readline-sync');

// let num1 = readlineSync.question('Digite um número: ');
// let num2 = readlineSync.question('Digite outro número: ');
// let operacao = readlineSync.question('Qual operação deseja fazer? (soma, subtração, divisão, multiplicação): ');

// num1 = parseFloat(num1);
// num2 = parseFloat(num2);

// let res;
// switch (operacao.toLowerCase()) {
//   case 'soma':
//     res = num1 + num2;
//     break;
//   case 'subtração':
//     res = num1 - num2;
//     break;
//   case 'divisão':
//     res = num1 / num2;
//     break;
//   case 'multiplicação':
//     res = num1 * num2;
//     break;
//   default:
//     console.log('Operação inválida.');
//     return;
// }

// console.log('O resultado é:', res);
