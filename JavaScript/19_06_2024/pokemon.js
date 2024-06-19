fetch("https://pokeapi.co/api/v2/pokemon/pikachu/")

.then(
    response => response.json()
)
.then(
    data => console.log(data.sprites.other.official-artwork
    )
)


// "sprites": {
//     "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/25.png",
//     "back_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/female/25.png",
//     "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/25.png",
//     "back_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/female/25.png",
//     "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
//     "front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/female/25.png",
//     "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/25.png",
//     "front_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/female/25.png",
//     "other": {
//       "dream_world": {
//         "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/25.svg",
//         "front_female": null
//       },
//   re   "official-artwork": {
//             "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
//             "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/shiny/25.png"

// https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png