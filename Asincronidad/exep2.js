const pokemon1= fetch("https://pokeapi.co/api/v2/pokemon/25");
const pokemon2= fetch("https://pokeapi.co/api/v2/pokemon/6");
const pokemon3= fetch("https://pokeapi.co/api/v2/pokemon/150");

Promise.any([pokemon1, pokemon2, pokemon3]).then(response=> {
    return response.json();
}).then(pokemon=> {
    console.log(pokemon.name);
}).catch(error=> {
    console.log("All request failed:", error);
});