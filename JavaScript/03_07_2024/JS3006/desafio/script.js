let frutas = [
  {
    nome: "Abacate",
    preco: 4.99,
    foto: "https://global.cdn.magazord.com.br/mondiniplantas/img/2021/07/produto/1277/muda-de-abacate-mondini-plantas.jpg?ims=800x800",
  },
  {
    nome: "Banana prata",
    preco: 2,
    foto: "https://ceagesp.gov.br/wp-content/uploads/2019/12/Banana_pratapng.png",
  },
  {
    nome: "Caju",
    preco: 29.99,
    foto: "https://global.cdn.magazord.com.br/vasoeflor/img/2024/01/produto/2033/caju-fruta-fundo-branco.jpg?ims=fit-in/800x800/filters:fill(white)",
  },
  {
    nome: "Laranja pera rio",
    preco: 4,
    foto: "https://tdc01z.vteximg.com.br/arquivos/ids/160294-1000-1000/21991-laranja-pera-rio-kg.png?v=637897733321300000",
  },
  {
    nome: "Goiaba",
    preco: 9.99,
    foto: "https://global.cdn.magazord.com.br/vasoeflor/img/2022/08/produto/1133/goiaba-tailandesa.jpg?ims=fit-in/800x800/filters:fill(white)",
  },
  {
    nome: "Jabuticaba",
    preco: 5,
    foto: "https://cdn.awsli.com.br/600x450/18/18885/produto/1972603/92ba3c993f.jpg",
  },
  {
    nome: "Morango",
    preco: 5,
    foto: "https://cdn.awsli.com.br/600x450/1348/1348550/produto/227378674/morango-lrfqi054sm.png",
  },
  {
    nome: "Maçã",
    preco: 5,
    foto: "https://superpao.vtexassets.com/unsafe/fit-in/720x720/center/middle/https%3A%2F%2Fsuperpao.vtexassets.com%2Farquivos%2Fids%2F432588%2FMaca-Importada-Vermelha-Kg.jpg%3Fv%3D638481844706070000",
  },
  {
    nome: "Pêssego",
    preco: 14.99,
    foto: "https://images.tcdn.com.br/img/img_prod/350075/muda_de_pessego_produzindo_pessegueiro_prunus_persica_162_1_20220412114228.jpg",
  },
  {
    nome: "Uva",
    preco: 5,
    foto: "https://www.proativaalimentos.com.br/image/cache/catalog/img_prod/uva[1]-1000x1000.jpg",
  },
];

const cards = document.getElementsByClassName('card')


frutas.forEach((fruta) => {
    const img = document.createElement('img')
    img.src = fruta
    galeria.appendChild(div)
});
