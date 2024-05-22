// Exercicio INCOMPLETO!!, finalizar os exercícios a seguir.

// DESAFIO: Sistema de Gerenciamento de Inventário
// Vamos criar um sistema de gerenciamento de inventário para uma loja. 
// Este sistema terá várias funcionalidades que utilizam as funções `map`, `join`, `reduce` e `filter`.

// EXERÍCICIOS
// 1. Exibir todos os produtos disponíveis.
//     Crie a função `displayAllProducts` itera sobre o array `products` e 
//     exibe cada produto em uma lista HTML.
    
// 2. Filtrar produtos por categoria:
//     Crie a função `filterByCategory` filtra os produtos com base na categoria inserida pelo usuário. 
//     Utiliza o método `filter` para criar um novo array de produtos que correspondem à 
//     categoria fornecida e exibe os produtos filtrados em uma lista HTML.
    
// 3. Calcular o valor total do inventário:
//   Crie a função `calculateTotalValue` utiliza o método `reduce` para calcular a 
//   soma dos preços de todos os produtos e exibe o valor total em um parágrafo HTML.

// 4. Listar todos os nomes de produtos em uma string única:
//   Crie a função `listProductNames` utiliza `map` para extrair os nomes dos produtos e 
//   `join` para concatenar esses nomes em uma string única, que é exibida em um parágrafo HTML.

const products = [
  { name: 'Laptop', price: 1500, category: 'Eletrônicos' },
  { name: 'Celular', price: 800, category: 'Eletrônicos' },
  { name: 'Camiseta', price: 30, category: 'Vestuário' },
  { name: 'Tênis', price: 100, category: 'Vestuário' },
  { name: 'Geladeira', price: 1200, category: 'Eletrodomésticos' },
  { name: 'Micro-ondas', price: 400, category: 'Eletrodomésticos' }
];

function filterByCategory(products, category) {
  return products.filter(product => product.category === category);
}

function displayProducts(products) {
  const productList = document.getElementById('productList');
  productList.innerHTML = ''; // Limpa a lista antes de adicionar os itens

  products.forEach(product => {
    const listItem = document.createElement('li');
    listItem.textContent = `${product.name} - ${product.price} - ${product.category}`;
    productList.appendChild(listItem);
  });
}

function calculateTotalValue(products) {
  const totalValue = products.reduce((accumulator, product) => accumulator + product.price, 0);
  return totalValue;
}

function listProductNames(products) {
  const productNames = products.map(product => product.name);
  return productNames.join(', ');
}

document.addEventListener('DOMContentLoaded', function() {
  const categoryForm = document.getElementById('categoryForm');
  const totalValueParagraph = document.getElementById('totalValue');
  const productNamesParagraph = document.getElementById('productNames');

  categoryForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const categoryInput = document.getElementById('category');
    const category = categoryInput.value;
    const filteredProducts = filterByCategory(products, category);
    displayProducts(filteredProducts);

    const totalValue = calculateTotalValue(filteredProducts);
    totalValueParagraph.textContent = `Valor Total: R$ ${totalValue.toFixed(2)}`;

    const allProductNames = listProductNames(filteredProducts);
    productNamesParagraph.textContent = `Nomes dos Produtos: ${allProductNames}`;
  });

  // Exibir todos os produtos inicialmente
  displayProducts(products);

  // Exibir o valor total inicialmente
  const totalValue = calculateTotalValue(products);
  totalValueParagraph.textContent = `Valor Total: R$ ${totalValue.toFixed(2)}`;
});
