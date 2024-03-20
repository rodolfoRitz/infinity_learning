numero = 10
if (numero % 2 === 0) {
    console.log('É par')
}

for (let i = 1; i < 11; i++) {
    if(i % 2 === 0){
        console.log(i)
    }
}

for (let i=0; i < 10; i++) {
    console.log(i)
}

for (let i=0; i < 10; i++) {
    if (i == 1){
        continue
    }
    console.log(i)
}
//////////////////////////////////////////////

let num = prompt('Digite um número inteiro: ')
res = 0
for (let num2=num; num < 11; num++) {
    res = 1*num2

    console.log(`1 x ${num2} = ${res}`)
}

numero = 10
if (numero % 2 === 0) {
    console.log('É par')
}

// resultado: 2,4,6,8,10
for (let i = 2; i < 11; i+=2) {
    console.log(i)
}
// resultado: 10,8,6,4,2
for (let i = 10; i >= 2;i-=2) {
    console.log(i)
}
////////////////////////////////////////////

// // 1,2,6,7,8,9,10
// for (let i = 1; i < 11; i++) {
//     if (i >= 3 && i <=5){
//         continue
//     } 
//     console.log(i)

// }

// 1,2,3,4,5,6,7
for (let i = 1; i <= 100; i++) {
    if(i > 7){
        break
    }
    console.log(i)
}


// console.log('ola')
const palavra = 'trambilique'

for (letra of palavra) {
    if (letra === 'i'){
        continue
    }
    else {
        console.log(letra)
    }
}
