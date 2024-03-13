// Turma 316
// https://messy-button-d76.notion.site/416c9d0f9cd346f3929ac9be24424036?v=a6e8284d6e9f44488ae525186a52e261
// Turma 416 (a minha)
// https://messy-button-d76.notion.site/Aula-2-Condicionais-01977a4f9fa64665b57bf9bf4774b1d5

let numero1 = Number(prompt('Digite um número: '));
let resto = numero1 % 2;

if      (numero1 < 0) { console.log('O número é inválido!') }
else if (resto === 0) { console.log('O número é PAR!'); }
else                  { console.log('O número é ÍMPAR!'); } 
