// Funções agregadoras, que percorrem um ARRAY: MAP, FILTER, REDUCE.
 
 /*Atividade 02
 Faça um Programa que mostre na tela apenas os número pares do
 seguinte array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] */
 const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
 const newArray_2 = array.filter(array => array % 2 === 0);
 console.log(newArray)

/*Atividade 03
 Faça um Programa que calcule a soma de todos os números do seguinte
 array [1, 2, 3, 4, 5, 6]*/
 const array_2 = [1, 2, 3, 4, 5, 6];
 const soma = array.reduce((acumulador, numero) => acumulador + numero,0);
 console.log(soma)

/*Atividade 04
 Dada uma lista de números imprima cada elemento elevado ao quadrado */
 const numbers_2 = [50, 45, 67, 89, 10, 5];
 const quadrado = numbers.map(number => number ** 2);
 console.log(quadrado)

/*Atividade 05
 Dada uma lista de strings, use a função map para criar uma nova lista
 onde cada string é convertida para maiúsculas*/
 const vogais = ["a", "b", "c", "d"];
 const upper = vogais.map(vogal => vogal.toUpperCase());
 console.log(upper);
 
/*Atividade 06
 Dada uma lista de strings, use a função filter para criar uma nova lista
 contendo apenas as palavras que têm mais de 5 caracteres*/
 const array_3 = ["vaca", "gaveta", "tenis", "infinity"];
 const newArray = array.filter(elemento => elemento.length > 5);
 console.log(newArray);

/* Faça um programa que mostre na tela o dobro de cada número do seguinte array [50, 45, 67, 89, 10, 5] */
 const numbers = [50, 45, 67, 89, 10, 5]
 const double = numbers.map(number => number * 2)
 console.log(double);


 /*DESAFIO PRÁTICO
 Crie um sistema simples de blog onde os usuários  podem visualizar postagens existentes, adicionar
 novas postagens e ver detalhes sobre cada postagem.
 Funcionalidades:
 Visualização de Postagens:
 Mostre ao usuário uma lista de postagens existentes com títulos e resumos.
 Detalhes da Postagem:
 Ao clicar em uma postagem, exiba o conteúdo completo da postagem, incluindo a data de
 publicação*/

